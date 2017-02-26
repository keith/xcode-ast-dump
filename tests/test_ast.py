import ast
import unittest

RAW_ARGUMENTS = open("tests/arguments.txt").read().strip().split()


class TestAST(unittest.TestCase):
    def test_removes_emits(self):
        _, other_arguments = ast.build_parser().parse_known_args(RAW_ARGUMENTS)
        for argument in other_arguments:
            self.assertNotIn("emit", argument)

    def test_adds_dump(self):
        command = ast.ast_command([])
        self.assertIn("-dump-ast", command)

    def test_starts_with_swiftc(self):
        command = ast.ast_command([])
        self.assertEqual(command[0], "swiftc")

    def test_ends_with_other_arguments(self):
        command = ast.ast_command(["foobar"])
        self.assertEqual(command[2], "foobar")
