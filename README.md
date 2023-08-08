# say11

`say11` is a command-line utility that leverages Eleven Labs' text-to-speech streaming API. You can easily convert text into speech right from your terminal using this handy tool. It's perfect for developers, content creators, or anyone looking to quickly turn text into audible content.

## Prerequisites

Before installing `say11`, ensure that you have `mpv` installed on your Mac. You can install it using [Homebrew](https://brew.sh/):

```sh
brew install mpv
```

```sh
pip install say11
```

Using say11 is incredibly simple. You can pipe text into the command from stdin, and it will use the Eleven Labs API to convert the text to speech. You can also specify a voice using the -v option.

## Examples

Read from a file and convert to speech:

```sh
cat text.txt | say11 -v Nicole 
```

```sh
echo "hello there everyone!" | say11 -v Nicole 
```

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request if you have any improvements or suggestions.

## Support
If you encounter any issues or need further assistance, please open an issue in the GitHub repository.