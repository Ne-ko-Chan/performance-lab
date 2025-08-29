import json
import sys

def get_value_by_id(values_json, id):
    for test_value in values_json:
        if test_value["id"] == id:
            return test_value["value"]

def match_values_recurcive(tests_json, values_json):
    for test in tests_json:
        if (lower := test.get("values")) != None:
            match_values_recurcive(lower, values_json)
        id = test["id"]
        test["value"] = get_value_by_id(values_json,id)

def form_report(testsfile: str, valuesfile: str, destfile: str) -> None:
    tests = open(testsfile, "r")
    values = open(valuesfile, "r")

    tests_json = json.load(tests)
    values_json = json.load(values)

    match_values_recurcive(tests_json["tests"], values_json["values"])
    res = open(destfile, "w")
    json.dump(tests_json, res)

    res.close()
    tests.close()
    values.close()

def main():
    if len(sys.argv) != 4:
        print("Wrong number of parameters, needs 3 file paths: tests.json, values.json, report.json")
        sys.exit(1)

    form_report(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
