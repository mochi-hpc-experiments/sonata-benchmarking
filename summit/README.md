How to run on Summit
====================

* Edit spack.yaml to change the path to sds-repo (you don't need to have added the sds namespace to spack).
* run `module load cmake` to get the native cmake on Summit
* In this folder, run `spack env activate .` then `spack install`.
* If your spack is not installed in $HOME/spack, edit run.qsub to source the correct path.
* If needed, edit the project allocation in run.qsub to use your allocation.
* Run `qsub run.qsub config.json` to submit the job. The benchmark outputs its results to standard output, which is redirected to a file prefixed with the cobalt job id.
