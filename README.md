# Average Image Color Tool
Tiny script for getting the average color of an image

## Usage

```sh
$ ./average_color.py <IMAGE_PATH>
```

## Add tool to path
- `chmod +x average_color`
  - Should already have been done, but might be an issue.
- `export PATH=~/<PATH-TO-REPO>/average_color:$PATH`
  - In order to use this throughout sessions, make sure to add it to `~/.bash_profile`, `~/.bashrc` or `~/.zshrc`.
- `average_color.py <IMAGE_PATH>`