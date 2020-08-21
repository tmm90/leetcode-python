# -*- coding: utf-8 -*-
import http.client
import json
import glob
import os
import sys
import argparse

G_BASE_PATH = None  # 基本路径


def get_leetcode_all_problems():
    #conn = http.client.HTTPSConnection("leetcode.com")
    conn = http.client.HTTPSConnection("leetcode-cn.com")
    conn.request("GET", "/api/problems/all/")

    response = conn.getresponse()
    if response.status != 200:
        return None

    data = json.JSONDecoder().decode(response.read().decode())
    problem_id_dict = {}
    for problem_info in data["stat_status_pairs"]:
        if problem_info["stat"]["question__hide"]:
            continue

        try:
            question_id = int(problem_info["stat"]["frontend_question_id"])
            question_name = problem_info["stat"]["question__title_slug"]
            problem_id_dict[question_id] = question_name
        except:
            continue

    return problem_id_dict


def create_source_file(problem_id):
    problem_id = int(problem_id)

    file_name = "%04d_*.py" % (problem_id)
    file_path = G_BASE_PATH + "src" + os.sep + file_name
    file_list = glob.glob(file_path)
    if file_list:
        print("file %s exists" % file_list[0].split(os.sep)[-1])
        sys.exit(0)

    problem_id_dict = get_leetcode_all_problems()
    if problem_id not in problem_id_dict:
        print("No problem %d" % problem_id)
        sys.exit(1)

    file_name = "%04d_%s.py" % (problem_id, problem_id_dict[problem_id])
    file_path = G_BASE_PATH + "src" + os.sep + file_name
    f = open(file_path, "w")
    f.close()
    print("create file %s." % file_name)
    sys.exit(0)


if __name__ == "__main__":
    if sys.argv[0].find(os.sep) < 0:
        G_BASE_PATH = '../'
    else:
        G_BASE_PATH, _, _ = sys.argv[0].rsplit(os.sep, 2)
        G_BASE_PATH += os.sep

    parser = argparse.ArgumentParser(description='leetcode-python toolbox.')

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    create_file_parser = subparsers.add_parser('create_file', aliases=['cf'])
    create_file_parser.add_argument('problem_id')
    args = parser.parse_args()
    if args != argparse.Namespace():
        create_source_file(args.problem_id)
