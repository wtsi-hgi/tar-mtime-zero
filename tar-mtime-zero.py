#!/usr/bin/env python

import tarfile
from sys import stdin, stdout

tar_in = tarfile.open(fileobj=stdin, mode="r|")
tar_out = tarfile.open(fileobj=stdout, mode="w|", format=tarfile.PAX_FORMAT)

for tarinfo in tar_in:
    tarinfo.mtime = 0
    tar_out.addfile(tarinfo, fileobj=tar_in.extractfile(tarinfo))

tar_in.close()
tar_out.close()
