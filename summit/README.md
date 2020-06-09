How to run on Summit
====================

* Edit spack.yaml to change the path to sds-repo (you don't need to have added the sds namespace to spack).
* run `module load cmake` to get the native cmake on Summit
* In this folder, run `spack env activate .` then `spack install`.
* If your spack is not installed in $HOME/spack, edit run.bsub to source the correct path.
* If needed, edit the project allocation in run.bsub to use your allocation.
* Run `bsub run.bsub` to submit the job. The benchmark outputs its results
  to a file named sonata-benchmarking.JOBID.
