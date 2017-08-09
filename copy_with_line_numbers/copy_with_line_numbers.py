import sublime, sublime_plugin
import os


def get_file_name(relative):
    view = sublime.Window.active_view(sublime.active_window())

    if not view.file_name():
        return "<unsaved>"
    else:
        filename = view.file_name()

    if relative:
        folders = sublime.Window.folders(sublime.active_window())
        if ( 0 < len( folders ) ):
            for folder in folders:
                if folder in filename:
                    filename = filename.replace(folder, '.')
                    break

    return filename


def get_line_num(obj, point):
    return obj.view.rowcol(point)[0] + 1


def create_output_body(obj, output):
    
    sels = obj.view.sel()

    # To print all the line numbers with the same length
    max_line_num = get_line_num(obj, sels[-1].end())
    max_line_num_len = len(str(max_line_num))
    format_string = "%0" + str(max_line_num_len) + "d: %s\n"

    # handle text
    isFollowupSelection = None
    for selection in sels:
        if isFollowupSelection:
            # split multi selections with ---
            output += "---\n"
        else:
            # but not the first one
            isFollowupSelection = True
        # for each selection
        selection = obj.view.line(selection)  # Extend selection to full lines
        first_line_num = get_line_num(obj, selection.begin())
        lines = obj.view.substr(selection).split("\n")  # Considers all line breaks
        for i, line in enumerate(lines):
            output += format_string % (first_line_num + i, line)

    return output


# FORMAT: TEXT
def create_text_output(obj, relative):
    
    filename = get_file_name(relative)

    # header - set file name
    output = "File: " + filename + "\n"
        
    # body
    output = create_output_body(obj, output)

    # send to clipboard
    sublime.set_clipboard(output)


# FORMAT: JIRA
def create_jira_output(obj, relative):

    filename = get_file_name(relative)

    # header - set file name
    # Need to replace DOS path \ with /
    output = "{code:java|titleBGColor=#F7D6C1|title=File: " + filename.replace("\\","&#92;" ) + "}\n"

    # body
    output = create_output_body(obj, output)

    # Footer
    output += '{code}'
    
    # send to clipboard
    sublime.set_clipboard(output)


# visibility
def is_relative_menu_visible():
        if ( 0 < len( sublime.Window.folders( sublime.active_window() ) ) ):
            if sublime.Window.active_view(sublime.active_window()).file_name():
                filename = sublime.Window.active_view(sublime.active_window()).file_name()
                
                # this is a saved file
                folders = sublime.Window.folders(sublime.active_window())
                if ( 0 < len( folders ) ):
                    for folder in folders:
                        if folder in filename:
                            return True
                    
                # we have a folder open but this file does not belong to it
                return False
            else:
                # this is a unsaved file
                return False
        else:
            # no folders in current window open
            return False


# command: "copy_with_line_numbers_text"
class CopyWithLineNumbersTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        output = create_text_output(self, False)


# command: "copy_with_line_numbers_text_relative"
class CopyWithLineNumbersTextRelativeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        create_text_output(self, True)

    def is_visible(self):
        return is_relative_menu_visible()


# command: "copy_with_line_numbers_jira"
class CopyWithLineNumbersJiraCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        create_jira_output(self, False)


# command: "copy_with_line_numbers_jira_relative"
class CopyWithLineNumbersJiraRelativeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        create_jira_output(self, True)

    def is_visible(self):
        return is_relative_menu_visible()

