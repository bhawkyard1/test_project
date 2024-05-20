name = "test_package"
version = "1.0.0"
build_command = ""
tests={
    "fail": {
        "command": "exit 1"
    },
    "fail_lst": {
        "command": ["exit", "1"]
    }
}
