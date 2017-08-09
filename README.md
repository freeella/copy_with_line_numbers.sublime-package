# copy_with_line_numbers.sublime-package
A sublime package to copy text with files name and numbers

<img src="CopyWithLineNumbersEditMenu.png" width="500">
<img src="CopyWithLineNumbersContextMenu.png" width="300">

## Install Sublime package Copy With Line Numbers

* Download [Copy With Line Numbers](https://github.com/freeella/copy_with_line_numbers.sublime-package/raw/master/Copy%20With%20Line%20Numbers.sublime-package)

* Place it inside the 'Installed Packages' directory.

````
[Linux]$ cp "Copy With Line Numbers.sublime-package" ~/.config/sublime-text-3/Installed\ Packages/


[OS X]$ cp "Copy With Line Numbers.sublime-package" ~/Library/Application\ Support/Sublime\ Text\ 3/Installed\ Packages/
or
[OS X]$ cp "Copy With Line Numbers.sublime-package" /Applications/Sublime\ Text.app/Contents/MacOS/Packages/


[WINDOWS]C:\> copy "Copy With Line Numbers.sublime-package" "%APPDATA%\Sublime Text 3\Installed Packages"
or
[WINDOWS]C:\> copy "Copy With Line Numbers.sublime-package" "%ProgramW6432%\Sublime Text 3\Packages"
````

* Restart Sublime

### Limitations

* If the package is deleted from "*/Installed Packages" by Package Control, deactivate "remove_orphaned" under 
"Package Settings"->"Package Control"->"Settings - User" or delete package-metadata.json.

```javascript
{
	"remove_orphaned": false
}
```

* When installing the package directly to the program directory, no packages are auto removed by Package Control but they might be removed when a Sublime Text is updated.
