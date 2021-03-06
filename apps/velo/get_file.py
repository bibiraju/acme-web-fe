import VeloAPI
import os
import sys


def get_file(remote_file_path, local_path, filename, site_user, velo_username, password):
    try:
        velo_api = VeloAPI.Velo()
        if not velo_api.isJVMStarted():
            velo_api.start_jvm()
        rs = velo_api.init_velo(velo_username, password)

        if velo_api.download_file(remote_file_path, local_path):
            content = open(local_path + filename).read()
            print content
            # c = content.splitlines(True)
            # for line in c:
            #     print line
        else:
            return -1
    except:
        raise


get_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
