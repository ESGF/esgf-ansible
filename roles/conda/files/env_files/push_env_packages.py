from __future__ import print_function
from subprocess import Popen, PIPE
import os
import sys
import shlex
import logging
import yaml
import click
from plumbum import local
from plumbum import TEE
from plumbum import BG
from plumbum.commands import ProcessExecutionError

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


with open(os.path.join(os.path.dirname(__file__), 'esgf-pub_env.yml'), 'r') as config_file:
    config = yaml.load(config_file)

# print("config:", config)
pip_dependencies = config["dependencies"][-1]
print("pip_dependencies:", pip_dependencies)
dependencies = config["dependencies"][:-1]
print("dependencies:", dependencies)

def call_binary(binary_name, arguments=None, silent=False, conda_env=None):
    '''Uses plumbum to make a call to a CLI binary.  The arguments should be passed as a list of strings'''
    RETURN_CODE = 0
    STDOUT = 1
    STDERR = 2
    logger.debug("binary_name: %s", binary_name)
    logger.debug("arguments: %s", arguments)
    if conda_env is not None:
        if arguments is not None:
            arguments = [conda_env, binary_name] + arguments
        else:
            arguments = [conda_env, binary_name]
        binary_name = os.path.join(os.path.dirname(__file__), "run_in_env.sh")
    try:
        command = local[binary_name]
    except ProcessExecutionError:
        logger.error("Could not find %s executable", binary_name)
        raise

    for var in os.environ:
        local.env[var] = os.environ[var]

    if silent:
        if arguments is not None:
            cmd_future = command.__getitem__(arguments) & BG
        else:
            cmd_future = command.run_bg()
        cmd_future.wait()
        output = [cmd_future.returncode, cmd_future.stdout, cmd_future.stderr]
    else:
        if arguments is not None:
            output = command.__getitem__(arguments) & TEE
        else:
            output = command.run_tee()

    #special case where checking java version is displayed via stderr
    if command.__str__() == '/usr/local/java/bin/java' and output[RETURN_CODE] == 0:
        return output[STDERR]

    #Check for non-zero return code
    if output[RETURN_CODE] != 0:
        logger.error("Error occurred when executing %s %s", binary_name, " ".join(arguments))
        logger.error("STDERR: %s", output[STDERR])
        raise ProcessExecutionError
    else:
        return output[STDOUT]

def run_cmd(cmd, verbose=False):
    if verbose:
        print("Executing :",cmd)
    p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    o,e = p.communicate()
    return o,e

@click.command()
@click.option('--env', default=None, help='Name of the conda environment for which to upload the packages it contains')
def main(env):

    env_file_name = "{}_env.yml".format(env)
    with open(os.path.join(os.path.dirname(__file__), env_file_name), 'r') as config_file:
        config = yaml.load(config_file)

    # print("config:", config)
    pip_dependencies = config["dependencies"][-1]
    print("pip_dependencies:", pip_dependencies)
    dependencies = config["dependencies"][:-1]
    print("dependencies:", dependencies)
    if sys.platform == "darwin":
        conda_os = "osx-64"
    else:
        conda_os = "linux-64"

    # sys.path.append("/anaconda2/bin")
    conda_pkgs = os.path.abspath(os.path.join(os.environ.get("CONDA_EXE"),"..","..","pkgs"))
    print("conda_pkgs:", conda_pkgs)
    # Get list of package we are using
    # pkgs = call_binary("conda", ["list", "-n", env_file_name])
    # print("test:", test)
    # pkgs, err = run_cmd("conda list", verbose=True)
    failed = []
    success = []
    # print("pkgs:", pkgs)
    # for l in pkgs.decode("utf8").split("\n")[2:-1]:
    print("Uploading packages for environment: {}".format(env_file_name))
    for dependency in dependencies:
        # print("l:", l)
        # sp = l.split()
        # name = sp[0]
        # # print("name:", name)
        # version = sp[1]
        # build = sp[2]
        name, version = dependency.split("=")
        print("name:", name)
        print("version:", version)
        # sys.exit(1)
        if name == "#":
            continue
        # tarname = "{}-{}-{}.tar.bz2".format(name,version,build)
        resource_location = "conda-forge/{}/{}".format(name, version)
        print("Copying {} version {}".format(name, version))
        try:
            output = call_binary("anaconda", ["copy", resource_location, "--to-owner", "esgf"])
            success.append((name, version))
        except ProcessExecutionError:
            failed.append((name, version))



    print("Successfully copied the following packages to the esgf conda channel")
    for package in success:
        print(package)

    print("The following packages failed to be copied.")
    for package in failed:
        print(package)
        # print("tarname:", tarname)
        # tarball = os.path.join(conda_pkgs,tarname)
        # print("looking at:",tarball,os.path.exists(tarball))
    #     if os.path.exists(tarball):
    #         o,e = run_cmd("anaconda upload {} -u esgf".format(tarball))
    #         print("OUT:",o.decode("utf8"))
    #         print("Err:",e.decode("utf8"))
    #     else:
    #         missing.append(tarball)
    # print(sys.prefix)
    # print(conda_pkgs)
    # print("Error on:",missing)
if __name__ == '__main__':
    main()
