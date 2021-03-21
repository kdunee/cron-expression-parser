# Crontab format
The format of a cron command is very much the V7 standard, with a number of upward-compatible extensions.

Each line has five time and date fields, followed by a user name (with optional ':group' and '/login-class' suffixes) if this is the system crontab file, followed by a command. You should run the task as a user with only the privileges it needs to run, and nothing else. For example, if you need to backup a database, don't just use the database root user, but use (or create) a specific user with only the rights needed to perform the backup.

You should test each command interactively on the command line, logged in as the user configured to run the task and with the appropriate environment set.

Each line in the cron table follows the following format:

    * * * * *  [UserName] Command_to_execute
    - – – – -
    | | | | |
    | | | | +—– Day of week (0–7) (Sunday=0 or 7) or Sun, Mon, Tue,…
    | | | +———- Month (1–12) or Jan, Feb,…
    | | +————-— Day of month (1–31)
    | +——————– Hour (0–23)
    +————————- Minute (0–59)
    There are several ways of specifying multiple values in a field:

- The asterisk (\*) operator specifies all possible values for a field. e.g. every hour or every day (first-last).
- The comma (,) operator specifies a list of values, for example: "1,3,4,7,8" The specified range is inclusive.
- The dash (-) operator specifies a range of values, for example: "1-6", which is equivalent to "1,2,3,4,5,6"
There is also an operator which some extended versions of cron support, the slash (/) operator, which can be used to skip a given number of values. For example, "\*/3" in the hour time field is equivalent to "0,3,6,9,12,15,18,21";
"\*" specifies 'every hour' but the "/3" means that only the first, fourth, seventh...and such values given by "\*" are used.

Step values can be used in conjunction with ranges. Following a range with '/number' specifies skips of the number's value through the range. For example, 0-23/2 can be used in the hours field to specify command execution every other hour (the alternative in the V7 standard is 0,2,4,6,8,10,12,14,16,18,20,22).
Steps are also permitted after an asterisk, so if you want to say 'every two hours', just use \*/2

Names can also be used for the 'month' and 'day of week' fields. Use the first three letters of the particular day or month (case doesn't matter). Ranges or lists of names are not allowed.

The 'sixth' field (the rest of the line) specifies the command to be run. The entire command portion of the line, up to a newline or % character, will be executed by /bin/sh or by the shell specified in the SHELL variable of the cronfile. Percent-signs (%) in the command, unless escaped with backslash (\), will be changed into newline characters, and all data after the first % will be sent to the command as standard input.

Instead of the first five fields, one of eight special strings can appear:

    string        meaning
    ------        -------
    @reboot      Run once, at startup.
    @yearly      Run once a year, "0 0 1 1 *".
    @annually     (sames as @yearly)
    @monthly      Run once a month, "0 0 1 * *".
    @weekly      Run once a week, "0 0 * * 0".
    @daily        Run once a day, "0 0 * * *".
    @midnight     (same as @daily)