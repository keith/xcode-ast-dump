import ast
import unittest

RAW_ARGUMENTS = open("tests/arguments.txt").read().strip().split()


class TestAST(unittest.TestCase):
    def test_removes_emits(self):
        _, other_arguments = ast.build_parser().parse_known_args(RAW_ARGUMENTS)
        for argument in other_arguments:
            self.assertNotIn("emit", argument)

    def test_adds_dump(self):
        command = ast.ast_command("", [])
        self.assertIn("-dump-ast", command)

    def test_starts_with_swiftc_argument(self):
        command = ast.ast_command("swiftc_arg", [])
        self.assertEqual(command[0], "swiftc_arg")

    def test_ends_with_other_arguments(self):
        command = ast.ast_command("", ["foobar"])
        self.assertEqual(command[2], "foobar")

    def test_swiftc_executable_path(self):
        environment = {"DEVELOPER_DIR": "/foo", "TOOLCHAINS": "com.bar"}
        swiftc = ast.swiftc_executable(environment)
        self.assertEqual(swiftc,
                         "/foo/Toolchains/bar.xctoolchain/usr/bin/swiftc")

    def test_swiftc_executable_path_override(self):
        environment = {"DEVELOPER_DIR": "/foo", "TOOLCHAINS": "com.bar",
                       "AST_SWIFTC": "bar"}
        swiftc = ast.swiftc_executable(environment)
        self.assertEqual(swiftc, "bar")

    def test_swift_executable_without_xcode(self):
        swiftc = ast.swiftc_executable({"AST_SWIFTC": "baz"})
        self.assertEqual(swiftc, "baz")

    def test_swift_executable_no_environ(self):
        swiftc = ast.swiftc_executable({})
        self.assertEqual(swiftc, "swiftc")

    def test_is_in_xcode(self):
        self.assertTrue(ast.is_in_xcode({"TOOLCHAINS": "is_set"}))

    def test_is_not_in_xcode(self):
        self.assertFalse(ast.is_in_xcode({}))
