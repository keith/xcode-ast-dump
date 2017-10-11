# xcode-ast-dump

This is a simple script for dumping the Swift AST from within Xcode.
Read more about how and why this works
[here](http://stackoverflow.com/a/42463996/902968).

## Usage

In Xcode:

1. In the build settings for the target that you're interested in
   dumping the AST for, set the `SWIFT_EXEC` user defined build setting
   to the path of `ast.py`.
1. Add `AST_DUMP_FILE="$(SRCROOT)/$(TARGET_NAME).ast"` to 
   `Preprocessor Macros`(`GCC_PREPROCESSOR_DEFINITIONS`) setting.
   You can put any path you want. This path will be used for saving build 
   log information with ast tree dump
1. Build the target
1. Check output file, you set in `AST_DUMP_FILE` setting.

In a shell:

1. Build your target normally
1. Go to the Report Navigator
1. Find the "Compile Swift Sources" step from your build (if it was an
   incremental build you may have to clean your project first)
1. Copy the arguments that were passed to `swiftc`
1. Escape any special characters such as `&` (Xcode escapes spaces but
   not special shell characters. In order to pass them to this script
   you'll have to escape them yourself)
1. Run `./ast.py ARGUMENTS > output.ast 2>&1`

### Notes

- For larger projects this will take a very long time to run and may
  cause Xcode to hang, if this happens it might be easier to run from a
  shell
- If you integrate the script in Xcode, the build will fail but the AST
  output will still be in the build log
- The larger the project, the larger the output, you may end up opening
  a very large file
- This script calls `swiftc` based on the environment variables from
  Xcode, or the first one that's found in your `$PATH`. This may not be
  what you expect. Set the `AST_SWIFTC` environment variable if you
  would like to change this
- This has only been tested with a small number of projects, please file
  any issues you find
