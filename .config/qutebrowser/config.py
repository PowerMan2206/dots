## PowerMan2206's badass config.py

## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

## load configs done via the GUI
config.load_autoconfig(True)

## no yucky default commands/aliases
c.bindings.default = {}
c.aliases = {}

c.auto_save.interval = 10000 # time interval (ms) between auto-saves of config/cookies/etc

## always restore open sites when qutebrowser is reopened. 
## `:wq` (`:quit --save`) to save it when this isn't used
c.auto_save.session = True


### COLORS

# color vars
bg = '#181b28' # bachground
bgb = '#212537' # background bright(er)
bgbb = '#6c7396' # background bright(er)(er)
fg = '#e8e7e4' # foreground
black = '#1c1b19'
yellow = '#fbb829'
red = '#ef2f27'
blue = '#2c78bf'
cyan = '#0aaeb3'
green = '#519f50'

## completion widget category header
c.colors.completion.category.bg = black
c.colors.completion.category.fg = fg
c.colors.completion.category.border.bottom = bg
c.colors.completion.category.border.top = black
## selected completion item
c.colors.completion.item.selected.bg = yellow
c.colors.completion.item.selected.fg = bg
c.colors.completion.item.selected.border.bottom = yellow
c.colors.completion.item.selected.border.top = yellow
c.colors.completion.item.selected.match.fg = red
c.colors.completion.match.fg = red
## background of the completion widget
c.colors.completion.odd.bg = bg
c.colors.completion.even.bg = bgb
## text of the completion widget
c.colors.completion.fg = [yellow, fg, fg]
## scrollbar in the completion view
c.colors.completion.scrollbar.bg = bgb
c.colors.completion.scrollbar.fg = bgbb

## context menu
c.colors.contextmenu.menu.bg = bgb
c.colors.contextmenu.menu.fg = fg
c.colors.contextmenu.disabled.bg = bg
c.colors.contextmenu.disabled.fg = fg
c.colors.contextmenu.selected.bg = bgbb
c.colors.contextmenu.selected.fg = fg

## download bar
c.colors.downloads.bar.bg = bg
c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = fg
## gradient start/stop for downloads
c.colors.downloads.start.bg = blue
c.colors.downloads.start.fg = fg
c.colors.downloads.stop.bg = green
c.colors.downloads.stop.fg = fg
## color gradient interpolation system for download backgrounds/foregrounds
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'
c.colors.downloads.system.fg = 'none'

## info message
c.colors.messages.info.bg = bgb
c.colors.messages.info.fg = fg
c.colors.messages.info.border = bgb
## warning message
c.colors.messages.warning.bg = yellow
c.colors.messages.warning.fg = bg
c.colors.messages.warning.border = yellow
## error message
c.colors.messages.error.bg = red
c.colors.messages.error.fg = fg
c.colors.messages.error.border = red

## prompts
c.colors.prompts.bg = bgb
c.colors.prompts.fg = fg
c.colors.prompts.border = '1px solid gray' # string
c.colors.prompts.selected.bg = bgbb

## tab bar
c.colors.tabs.bar.bg = bg
## selected tabs
c.colors.tabs.selected.odd.bg = bgbb
c.colors.tabs.selected.odd.fg = fg
c.colors.tabs.selected.even.bg = bgbb
c.colors.tabs.selected.even.fg = fg
## unselected tabs
c.colors.tabs.odd.bg = bg
c.colors.tabs.odd.fg = fg
c.colors.tabs.even.bg = bgb
c.colors.tabs.even.fg = fg
## tab indicator
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = green
c.colors.tabs.indicator.error = red
## color gradient interpolation system for the tab indicator
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## statusbar
c.colors.statusbar.normal.bg = bg
c.colors.statusbar.normal.fg = fg
c.colors.statusbar.url.fg = fg
c.colors.statusbar.url.hover.fg = cyan
c.colors.statusbar.url.warn.fg = yellow
c.colors.statusbar.url.error.fg = red
c.colors.statusbar.url.success.http.fg = fg
c.colors.statusbar.url.success.https.fg = green
## statusbar/commandbar in private browsing mode
c.colors.statusbar.private.bg = 'purple'
c.colors.statusbar.private.fg = fg
c.colors.statusbar.command.private.bg = 'purple'
c.colors.statusbar.command.private.fg = fg
## statusbar in command mode
c.colors.statusbar.command.bg = bg
c.colors.statusbar.command.fg = fg
## statusbar in insert mode
c.colors.statusbar.insert.bg = yellow
c.colors.statusbar.insert.fg = bg
## statusbar in passthrough mode
c.colors.statusbar.passthrough.bg = blue
c.colors.statusbar.passthrough.fg = fg
## statusbar in caret mode
c.colors.statusbar.caret.bg = 'purple'
c.colors.statusbar.caret.fg = fg
c.colors.statusbar.caret.selection.bg = '#a12dff'
c.colors.statusbar.caret.selection.fg = fg

c.colors.statusbar.progress.bg = bg # background of the progress bar

c.colors.webpage.bg = bg # empty webpages


### DARK MODE

c.colors.webpage.darkmode.enabled = True # render all web contents using a dark theme

## which algorithm to use
##   - lightness-cielab: Modify colors by converting them to CIELAB color space and inverting the L value. Not available with Qt < 5.14.
##   - lightness-hsl: Modify colors by converting them to the HSL color space and inverting the lightness (i.e. the "L" in HSL).
##   - brightness-rgb: Modify colors by subtracting each of r, g, and b from their maximum value.
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'

c.colors.webpage.darkmode.contrast = 0.0 # contrast, only when `lightness-hsl` or `brightness-rgb` is used

## when to use dark mode
##   - always: Apply dark mode filter to all frames, regardless of content.
##   - smart: Apply dark mode filter to frames based on background color.
c.colors.webpage.darkmode.policy.page = 'smart'

## value to use for `prefers-color-scheme:` for websites
##   - auto: Use the system-wide color scheme setting.
##   - light: Force a light theme.
##   - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = 'dark'

## render all colors as grayscale
c.colors.webpage.darkmode.grayscale.all = False
c.colors.webpage.darkmode.grayscale.images = 0.0 # desaturation factor for images, 1 is grayscale

## when to apply dark mode to images
##   - always: Apply dark mode filter to all images.
##   - never: Never apply dark mode filter to any images.
##   - smart: Apply dark mode based on image content. Not available with Qt 5.15.0.
c.colors.webpage.darkmode.policy.images = 'never'

## threshold for inverting background elements with dark mode
c.colors.webpage.darkmode.threshold.background = 128 # opposite of `colors.webpage.darkmode.threshold.text`
## threshold for inverting text with dark mode
c.colors.webpage.darkmode.threshold.text = 128


### COMMAND/COMPLETION STUFF

## when to show the autocompletion window.
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
c.completion.show = 'always'

## number of commands to save in the command history
## 0 - no history, -1 - unlimited
c.completion.cmd_history_max_items = 50

## delay (ms) before updating completions after typing a character
c.completion.delay = 0

## default filesystem autocomplete suggestions for :open
## idk how this works
# c.completion.favorite_paths = []

## height (px or % of the window) of the completion
c.completion.height = '40%'

## minimum amount of characters needed to update completions
c.completion.min_chars = 1

## which categories to show (in which order) in the :open completion
##   - searchengines
##   - quickmarks
##   - bookmarks
##   - history
##   - filesystem
c.completion.open_categories = ['searchengines', 'quickmarks', 'history']

c.completion.quick = True # move on to the next part (?) when there's only one possible completion left

## completion window scrollbar (px)
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 6

c.completion.shrink = False # shrink the completion to be smaller than the configured size if there are no scrollbars

c.completion.timestamp_format = '%Y-%m-%d %H:%M:%S' # format of timestamps

c.completion.use_best_match = False # execute the best-matching command on a partial match

## a list of patterns which should not be shown in the history completion
## (but will in history)
# c.completion.web_history.exclude = []

## Number of URLs to show in the web history
## 0 - no history, -1 - unlimited
c.completion.web_history.max_items = -1


### PRIVACY/SECURITY

c.content.blocking.enabled = True # enable the ad/host blocker

## which method of blocking ads should be used
##   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
##   - adblock: Use Brave's ABP-style adblocker
##   - hosts: Use hosts blocking
##   - both: Use both hosts blocking and Brave's ABP-style adblocker
c.content.blocking.method = 'adblock'

## list of URLs to host blocklists for the host blocker 
# c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

## list of URLs to ABP-style adblocking rulesets
c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt']

# c.content.blocking.whitelist = [] # a list of patterns that should always be loaded, despite the ad/host-blocker

## proxy to use
##   - `socks://`, `http://`, whatever
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
c.content.proxy = 'none'

## user agent to send
# c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'
c.content.headers.user_agent = 'oh nywo u fwound my usew agent OwO what wiww i dwo' # funk you lom

c.content.canvas_reading = False # allow websites to read canvas elements

# c.content.cache.size = None # size (b) of the HTTP network cache, null to use the default value

c.content.cookies.store = True # store cookies
## which cookies to accept
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
##   - never: Don't accept cookies at all.
c.content.cookies.accept = 'no-3rdparty'

c.content.default_encoding = 'utf-8' # default encoding to use for websites

## allow websites to share screen content
##   - true
##   - false
##   - ask
c.content.desktop_capture = 'ask'

## allow websites to request geolocations
##   - true
##   - false
##   - ask
c.content.geolocation = 'ask'

c.content.dns_prefetch = True # try to pre-fetch DNS entries to speed up browsing

c.content.headers.accept_language = 'en-US,en;q=0.9' # value to send in the `Accept-Language` header

# c.content.headers.custom = {} # custom headers for qutebrowser HTTP requests.

c.content.headers.do_not_track = True # value to send in the `DNT` header

## when to send the Referer header
##   - always: Always send the Referer.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
c.content.headers.referer = 'same-domain'

c.content.hyperlink_auditing = False # enable hyperlink auditing (`<a ping>`) (??)

c.content.autoplay = False # automatically start playing `<video>` elements
c.content.images = True # automatically load images

c.content.javascript.enabled = True # enable JavaScript 😔
c.content.javascript.alert = True # show JavaScript alerts
c.content.javascript.prompt = True # show JavaScript prompts
c.content.javascript.can_access_clipboard = False # allow JavaScript to read from or write to the clipboard
c.content.javascript.can_open_tabs_automatically = False # allow JavaScript to open new tabs without user interaction
## log levels to use for JavaScript console logging messages
## valid: `none`, `debug`, `info`, `warning`, `error`
c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}
c.content.javascript.modal_dialog = False # use the standard JavaScript modal dialog for `alert()` and `confirm()`

## allow locally loaded documents to access local/remote URLs
c.content.local_content_can_access_file_urls = True
c.content.local_content_can_access_remote_urls = False

c.content.local_storage = True # enable support for HTML 5 local storage and Web SQL

## allow websites to request persistent storage quota via `navigator.webkitPersistentStorage.requestQuota`
##   - true
##   - false
##   - ask
c.content.persistent_storage = 'ask'

## allow websites to register protocol handlers via `navigator.registerProtocolHandler`
##   - true
##   - false
##   - ask
c.content.register_protocol_handler = 'ask'

## allow websites to record audio/video/audio and video
##   - true
##   - false
##   - ask
c.content.media.audio_capture = 'ask'
c.content.media.video_capture = 'ask'
c.content.media.audio_video_capture = 'ask'

## allow websites to lock your mouse pointer
##   - true
##   - false
##   - ask
c.content.mouse_lock = 'ask'

## Allow websites to show notifications.
##   - true
##   - false
##   - ask
c.content.notifications.enabled = 'ask'

# c.content.netrc_file = None # netrc-file for HTTP authentication, if unset, `~/.netrc` is used (??)

## what notification presenter to use for web notifications
##   - auto: Tries `libnotify`, `systray` and `messages`, uses the first one available without showing error messages.
##   - qt: Use Qt's native notification presenter, based on a system tray icon. Switching from or to this value requires a restart of qutebrowser. Recommended over `systray` on PyQt 5.14.
##   - libnotify: Shows messages via DBus in a libnotify-compatible way. If DBus isn't available, falls back to `systray` or `messages`, but shows an error message.
##   - systray: Use a notification presenter based on a systray icon. Falls back to `libnotify` or `messages` if not systray is available. This is a reimplementation of the `qt` setting value, but with the possibility to switch to it at runtime.
##   - messages: Show notifications as qutebrowser messages. Most notification features aren't available.
##   - herbe: (experimental!) Show notifications using herbe (github.com/dudik/herbe). Most notification features aren't available.
c.content.notifications.presenter = 'libnotify'

c.content.notifications.show_origin = False # whether to show the origin URL for notifications

c.content.plugins = False # enable plugins in Web pages

c.content.print_element_backgrounds = True # draw the background color and images also when the page is printed

c.content.private_browsing = False # open new windows in private browsing mode 

c.content.site_specific_quirks.enabled = False # enable quirks

## how to proceed on TLS certificate errors
##   - ask: Ask how to proceed for every certificate error (unless non-overridable due to HSTS).
##   - ask-block-thirdparty: Ask how to proceed for normal page loads, but silently block resource loads.
##   - block: Automatically block loading on certificate errors.
##   - load-insecurely: Force loading pages despite certificate errors. This is *insecure* and should be avoided. Instead of using this, consider fixing the underlying issue or importing a self-signed certificate via `certutil` (or Chromium) instead.
c.content.tls.certificate_errors = 'ask'

## how navigation requests to URLs with unknown schemes are handled
##   - disallow: Disallows all navigation requests to URLs with unknown schemes.
##   - allow-from-user-interaction: Allows navigation requests to URLs with unknown schemes that are issued from user-interaction (like a mouse-click), whereas other navigation requests (for example from JavaScript) are suppressed.
##   - allow-all: Allows all navigation requests to URLs with unknown schemes.
c.content.unknown_url_scheme_policy = 'allow-from-user-interaction'

c.content.webgl = True # enable WebGL
## which interfaces to expose via WebRTC.
##   - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
##   - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
##   - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
##   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
c.content.webrtc_ip_handling_policy = 'all-interfaces'

## monitor load requests for cross-site scripting attempts
## bypasses for this are widely known and it can be abused for cross-site info leaks
c.content.xss_auditing = False


### DOWNLOADING

## directory to save downloads to
## if unset, a sensible OS default is used
# c.downloads.location.directory = None

c.downloads.location.prompt = True # prompt the user for the download location
c.downloads.location.remember = False # remember the last used download location

## what to display in the download filename input
##   - path: Show only the download path.
##   - filename: Show only download filename.
##   - both: Show download path and filename.
c.downloads.location.suggestion = 'both'

## default program used to open downloads. 
## if null, the default internal handler is used.
# c.downloads.open_dispatcher = None

## where to show the downloaded files
##   - top
##   - bottom
c.downloads.position = 'bottom'

c.downloads.remove_finished = 75000 # duration (ms) to wait before removing finished downloads


### Yeah I just nuked all hint stuff, I don't like hints


### FONTS

c.fonts.default_family = ["monospace"] # default font families to use
c.fonts.default_size = '9pt' # default font size to use

c.fonts.completion.category = 'bold default_size default_family' # completion categories
c.fonts.completion.entry = 'default_size default_family' # completion widget
c.fonts.contextmenu = 'default_size default_family' # context menu
c.fonts.debug_console = 'default_size default_family' # debugging console
c.fonts.downloads = 'default_size default_family' # downloadbar
c.fonts.messages.error = 'default_size default_family' # error messages
c.fonts.messages.info = 'default_size default_family' # info messages
c.fonts.messages.warning = 'default_size default_family' # warning messages
c.fonts.prompts = 'default_size default_family' # prompts
c.fonts.statusbar = 'default_size default_family' # statusbar
c.fonts.tabs.selected = 'default_size default_family' # selected tabs
c.fonts.tabs.unselected = 'default_size default_family' # unselected tabs

## font families
c.fonts.web.family.cursive = 'monospace' # cursive fonts
c.fonts.web.family.fantasy = 'monospace' # fantasy fonts
c.fonts.web.family.fixed = 'monospace' # fixed fonts
c.fonts.web.family.sans_serif = 'monospace' # sans-serif fonts
c.fonts.web.family.serif = 'monospace' # serif fonts
c.fonts.web.family.standard = 'monospace' # standard fonts

## default font sizes (px)
c.fonts.web.size.default = 15
c.fonts.web.size.default_fixed = 13
c.fonts.web.size.minimum = 4
c.fonts.web.size.minimum_logical = 6 # when zooming out


### STATUSBAR AND TABS

c.statusbar.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0} # padding (px) for the statusbar

## position of the status bar
##   - top
##   - bottom
c.statusbar.position = 'bottom'

## when to show the statusbar
##   - always: Always show the statusbar.
##   - never: Always hide the statusbar.
##   - in-mode: Show the statusbar when in modes other than normal mode.
c.statusbar.show = 'always'

## list of widgets displayed in the statusbar
##   - url: Current page URL.
##   - scroll: Percentage of the current page position like `10%`.
##   - scroll_raw: Raw percentage of the current page position like `10`.
##   - history: Display an arrow when possible to go back/forward in history.
##   - tabs: Current active tab, e.g. `2`.
##   - keypress: Display pressed keys when composing a vi command.
##   - progress: Progress bar for the current page loading.
##   - text:foo: Display the static text after the colon, `foo` in the example.
c.statusbar.widgets = ['keypress', 'url', 'history', 'scroll']#, 'progress']

## maximum/minimum width (px) of tabs 
## -1 for no maximum/default minimum size behaviour
c.tabs.max_width = -1
c.tabs.min_width = -1

c.tabs.background = True # open new tabs (middleclick/ctrl+click) in the background

## mouse button with which to close tabs
##   - right: Close tabs on right-click.
##   - middle: Close tabs on middle-click.
##   - none: Don't close tabs using the mouse.
c.tabs.close_mouse_button = 'middle'

## how to behave when the close mouse button is pressed on the tab bar
##   - new-tab: Open a new tab.
##   - close-current: Close the current tab.
##   - close-last: Close the last tab.
##   - ignore: Don't do anything.
c.tabs.close_mouse_button_on_bar = 'new-tab' # not like I'm gonna use this lol

c.tabs.favicons.scale = 1.2 # scaling factor for favicons in the tab bar

## when to show favicons in the tab bar
##   - always: Always show favicons.
##   - never: Always hide favicons.
##   - pinned: Show favicons only on pinned tabs.
c.tabs.favicons.show = 'always'

c.tabs.focus_stack_size = -1 # maximum stack size to remember for tab switches, -1 for no maximum

c.tabs.indicator.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 3} # padding (px) for tab indicators

c.tabs.indicator.width = 3 # width (px) of the progress indicator, 0 to disable

## how to behave when the last tab is closed
##   - ignore: Don't do anything.
##   - blank: Load a blank page.
##   - startpage: Load the start page.
##   - default-page: Load the default page.
##   - close: Close the window.
c.tabs.last_close = 'close'

## when switching tabs, what input mode is applied
##   - persist: Retain the current mode.
##   - restore: Restore previously saved mode.
##   - normal: Always revert to normal mode.
c.tabs.mode_on_change = 'normal'

c.tabs.mousewheel_switching = True # switch between tabs using the mouse wheel

## position of new tabs opened from another tab
##   - prev: Before the current tab.
##   - next: After the current tab.
##   - first: At the beginning.
##   - last: At the end.
c.tabs.new_position.related = 'next'

c.tabs.new_position.stacking = False # stack related tabs on top of each other when opened consecutively

## position of new tabs which are not opened from another tab
##   - prev: Before the current tab.
##   - next: After the current tab.
##   - first: At the beginning.
##   - last: At the end.
c.tabs.new_position.unrelated = 'last'

c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 5} # padding (px) around text for tabs

## position of the tab bar
##   - top
##   - bottom
##   - left
##   - right
c.tabs.position = 'top'

## which tab to select when the focused tab is removed
##   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
##   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
##   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'

## when to show the tab bar
##   - always: Always show the tab bar.
##   - never: Always hide the tab bar.
##   - multiple: Hide the tab bar if only one tab is open.
##   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'

# c.tabs.show_switching_delay = 800 # duration (ms) to show the tab bar before hiding it when tabs.show is set to 'switching'

c.tabs.tabs_are_windows = False # open a new window for every tab

## alignment of the text inside of tabs
##   - left
##   - right
##   - center
c.tabs.title.alignment = 'left'

## format to use for the tab title
## there was a lotta placeholders here but I nuked them
c.tabs.title.format = '{audio}{private}{index}: {current_title}'

c.tabs.tooltips = True # show tooltips on tabs

c.tabs.undo_stack_size = -1 # number of closed tabs (per window) and closed windows to remember for :undo, -1 for no maximum

# c.tabs.width = '15%' # width (px or % of the window) of the tab bar if it's vertical

c.tabs.wrap = True # wrap when changing tabs

## how to open links in an existing instance if a new one is launched
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
##   - private-window: Open in a new private window.
c.new_instance_open_target = 'tab'

## which window to choose when opening links as new tabs
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
c.new_instance_open_target_window = 'last-focused'


### NERD STUFF

c.input.escape_quits_reporter = True # allow esc to quit the crash reporter

## level for console (stdout/stderr) logs, ignored if `--loglevel` or `--debug` are used
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
c.logging.level.console = 'info'

## level for in-memory logs
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
c.logging.level.ram = 'debug'

# c.qt.args = [] # additional arguments to pass to Qt, without leading `--`
# c.qt.environ = {} # additional environment variables to set

## force a Qt platform to use, sets the `QT_QPA_PLATFORM` environment variable
## usually for wayland but it's already native so
# c.qt.force_platform = None

# c.qt.force_platformtheme = None # force a Qt platformtheme to use, sets the `QT_QPA_PLATFORMTHEME` environment variable

## force software rendering for QtWebEngine, needed for Nouveau drivers
##   - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
##   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
##   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
##   - none: Don't force software rendering.
c.qt.force_software_rendering = 'chromium'

c.qt.highdpi = True # turn on Qt HighDPI scaling

## when to use Chromium's low-end device mode
##   - always: Always use low-end device mode.
##   - auto: Decide automatically (uses low-end mode with < 1 GB available RAM).
##   - never: Never use low-end device mode.
c.qt.low_end_device_mode = 'never'

## which Chromium process model to use
##   - process-per-site-instance: Pages from separate sites are put into separate processes and separate visits to the same site are also isolated.
##   - process-per-site: Pages from separate sites are put into separate processes. Unlike Process per Site Instance, all visits to the same site will share an OS process. The benefit of 
##                       this model is reduced memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
##   - single-process: Run all tabs in a single process. This should be used for debugging purposes only, and it disables `:open --private`.
c.qt.process_model = 'process-per-site-instance'

c.qt.workarounds.remove_service_workers = False # delete the QtWebEngine Service Worker directory on every start

# c.session.default_name = None # name of the session to save by default

# c.session.lazy_restore = False # load a restored tab as soon as it takes focus

# c.content.user_stylesheets = [] # list of user stylesheet filenames to use, uhhhhh

c.editor.command = ['alacritty', '-e', 'micro', '{file}'] # editor (and arguments) to use for the `edit-*` commands
c.editor.encoding = 'utf-8' # encoding to use for the editor

## backend to use to display websites
##   - webengine: Use QtWebEngine (based on Chromium - recommended).
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari - many known security issues!).
c.backend = 'webengine'

## when to show a changelog after qutebrowser was upgraded
##   - major: Show changelog for major upgrades (e.g. v2.0.0 -> v3.0.0).
##   - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 -> v2.1.0).
##   - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 -> v2.0.1).
##   - never: Never show changelog after upgrades.
c.changelog_after_upgrade = 'patch'


### OTHER STUFF

## maximum time (min) between two history items for them to be
## considered being from the same browsing session
c.history_gap_interval = 20

## which unbound keys to forward to the webview in normal mode
##   - all: Forward all unbound keys.
##   - auto: Forward unbound non-alphanumeric keys.
##   - none: Don't forward any keys.
c.input.forward_unbound_keys = 'all'

## leave/enter insert mode if an non-/editable element is clicked
c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True
c.input.insert_mode.auto_load = False # auto enter insert mode if an editable element is focused after loading the page
c.input.insert_mode.leave_on_load = True # leave insert mode when starting a new page load
c.input.insert_mode.plugins = False # switch to insert mode when clicking flash and other plugins

# c.input.links_included_in_focus_chain = True # Include hyperlinks in the keyboard focus chain when tabbing

c.input.media_keys = False # whether the underlying Chromium should handle media keys

c.input.mouse.back_forward_buttons = True # enable back and forward buttons on the mouse

## enable Opera-like mouse rocker gestures
## disables the context menu
c.input.mouse.rocker_gestures = False

c.input.partial_timeout = 0 # timeout (ms) for partially typed key bindings

c.input.spatial_navigation = True # enable spatial navigation (arrow keys to navigate a page)

c.messages.timeout = 5000 # duration (ms) to show messages in the statusbar for, 0 to never clear messages

c.prompt.filebrowser = True # show a filebrowser in download prompts
c.prompt.radius = 0 # rounding radius (in pixels) for the edges of prompts

c.scrolling.smooth = False # enable smooth scrolling for web pages, does not work with`:scroll-px`
## when/how to show the scrollbar
##   - always: Always show the scrollbar.
##   - never: Never show the scrollbar.
##   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
##   - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
c.scrolling.bar = 'overlay'

c.search.incremental = True # find text on a page incrementally, renewing the search for each typed character
c.search.wrap = True # wrap around at the top and bottom of the page when advancing through search
## when to find text on a page case-insensitively
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
c.search.ignore_case = 'smart'

c.spellcheck.languages = ["hr-HR", "en-US"] # languages to use for spell checking

## require a confirmation before quitting
##   - always: Always show a confirmation.
##   - multiple-tabs: Show a confirmation if multiple tabs are opened.
##   - downloads: Show a confirmation if downloads are running
##   - never: Never show a confirmation.
c.confirm_quit = ['downloads']

c.content.fullscreen.overlay_timeout = 0 # set fullscreen notification overlay timeout in milliseconds
c.content.fullscreen.window = False # limit fullscreen to the browser window (does not expand to fill the screen)

## what search to start when something else than a URL is entered
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
##   - schemeless: Always search automatically unless URL explicitly contains a scheme.
c.url.auto_search = 'naive'

c.content.pdfjs = True # allow pdf.js to view PDF files in the browser

c.content.mute = False # automatically mute tabs

c.url.default_page = 'about:blank' # page to open if :open -t/-b/-w is used without URL

# c.url.open_base_url = False # open base URL of the searchengine if a searchengine shortcut is invoked without parameters

c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'} # search engines which can be used via the address bar, {} is the search query

c.url.start_pages = ['about:blank'] # page(s) to open at the start

c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'] # URL parameters to strip with `:yank url`

# c.window.hide_decoration = False # hide the window decoration, imagine having those
# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser' # format to use for the window title, i laugh

c.window.transparent = False # set the main window background to transparent

c.zoom.default = '90%' # default zoom level
c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%'] # available zoom levels

## number of zoom increments to divide the mouse wheel movements to
# c.zoom.mouse_divider = 512


### BINDS

config.bind('<Alt-1>', 'tab-focus 1')
config.bind('<Alt-2>', 'tab-focus 2')
config.bind('<Alt-3>', 'tab-focus 3')
config.bind('<Alt-4>', 'tab-focus 4')
config.bind('<Alt-5>', 'tab-focus 5')
config.bind('<Alt-6>', 'tab-focus 6')
config.bind('<Alt-7>', 'tab-focus 7')
config.bind('<Alt-8>', 'tab-focus 8')
config.bind('<Alt-9>', 'tab-focus -1')
config.bind('<Alt-m>', 'tab-mute')

## normal mode
config.bind(':', 'set-cmd-text :')
config.bind('c', 'config-source')
config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
config.bind('<Alt+Left>', 'tab-prev')
config.bind('<Alt+Right>', 'tab-next')
config.bind('<Ctrl+Alt+Left>', 'tab-move -')
config.bind('<Ctrl+Alt+Right>', 'tab-move +')
config.bind('y', 'yank')
config.bind('+', 'zoom')     # do
config.bind('=', 'zoom-in')  # not
config.bind('-', 'zoom-out') # ask
config.bind('g', 'set-cmd-text :open {url:pretty}')
config.bind('o', 'set-cmd-text -s :open')
config.bind('O', 'set-cmd-text -s :open -t')
config.bind('u', 'undo')
config.bind('U', 'undo -w')
config.bind('b', 'set-cmd-text -s :quickmark-load -t')
config.bind('B', 'set-cmd-text -s :quickmark-load')
config.bind('<Ctrl+B>', 'set-cmd-text -s :quickmark-add {url}')
config.bind('x', 'set-cmd-text -s :tab-give')
config.bind('h', 'history -t')
config.bind('f', 'set-cmd-text /')
config.bind('<Ctrl+F>', 'set-cmd-text ?')
config.bind('n', 'search-next')
config.bind('p', 'search-prev')
config.bind('<Ctrl+A>', 'mode-enter caret ;; selection-toggle ;; move-to-end-of-document')
config.bind('r', 'reload')
config.bind('<Ctrl+R>', 'reload -f')
config.bind('<f11>', 'fullscreen')
config.bind('<f12>', 'devtools right')
config.bind('<Ctrl+Q>', 'quit')
config.bind('n', 'open -w')
config.bind('<Ctrl+T>', 'open -t')
config.bind('<Ctrl+D>', 'tab-clone')
config.bind('<Ctrl+N>', 'open -p')
config.bind('<Ctrl+Shift+W>', 'close')
config.bind('<Ctrl+V>', 'mode-enter passthrough')
config.bind('<Ctrl+W>', 'tab-close')
config.bind('<Ctrl+Up>', 'scroll-to-perc 0')
config.bind('<Ctrl+Down>', 'scroll-to-perc 100')

## command mode
config.bind('<Up>', 'completion-item-focus prev', mode='command')
config.bind('<Down>', 'completion-item-focus next', mode='command')
config.bind('<Return>', 'command-accept', mode='command')
config.bind('<Tab>', 'completion-item-focus next', mode='command')
config.bind('<Escape>', 'mode-leave', mode='command')

## insert mode, not much more needed, eh?
config.bind('<Escape>', 'mode-leave', mode='insert')

## passthrough mode
config.bind('<Shift-Escape>', 'mode-leave', mode='passthrough')

## caret mode, I literally just use this for Ctrl+A
config.bind('<Escape>', 'mode-leave', mode='caret')

## prompt mode
config.bind('<Escape>', 'mode-leave', mode='prompt')
config.bind('<Return>', 'prompt-accept', mode='prompt')
config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')

## register mode, whatever it is
config.bind('<Escape>', 'mode-leave', mode='register')

## yesno mode
config.bind('y', 'prompt-accept yes', mode='yesno')
config.bind('Y', 'prompt-accept --save yes', mode='yesno')
config.bind('n', 'prompt-accept no', mode='yesno')
config.bind('N', 'prompt-accept --save no', mode='yesno')
config.bind('<Escape>', 'mode-leave', mode='yesno')
config.bind('<Return>', 'prompt-accept', mode='yesno')
