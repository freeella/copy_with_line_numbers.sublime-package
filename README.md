# copy_with_line_numbers.sublime-package
A sublime package to copy text with files name and numbers

## Install Sublime package Copy With Line Numbers

* Download [Copy With Line Numbers](https://github.com/freeella/copy_with_line_numbers.sublime-package/raw/master/Copy%20With%20Line%20Numbers.sublime-package)

* Place it inside the 'Installed Packages' directory.

````
[Linux]$ cp copy_with_line_numbers.sublime-package ~/.config/sublime-text-2/Installed\ Packages/

[OS X]$ cp copy_with_line_numbers.sublime-package ~/Library/Application\ Support/Sublime\ Text\ 3/Installed\ Packages/

[WINDOWS]C:\> copy copy_with_line_numbers.sublime-package "%APPDATA%\Sublime Text 3\Installed Packages"
or
[WINDOWS]C:\> copy copy_with_line_numbers.sublime-package "%ProgramW6432%\Sublime Text 3\Packages"
````

* Restart Sublime

* If the package is deleted on restart, deactivate "remove_orphaned" under 
"Package Settings"->"Package Control"->"Settings - User" or delete package-metadata.json.

```javascript
{
	"remove_orphaned": false
}
```
