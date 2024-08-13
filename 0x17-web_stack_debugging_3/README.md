# Web Stack Debugging: Fixing a 500 Error on a WordPress Site

## Overview

This project focuses on debugging a WordPress site running on a LAMP (Linux, Apache, MySQL, PHP) stack. The site was experiencing an HTTP 500 Internal Server Error due to a misconfiguration in the `wp-settings.php` file. The goal is to identify the root cause of the issue, fix it, and automate the solution using a Puppet manifest.

## Prerequisites

- Ubuntu 14.04 LTS
- Puppet 3.4
- Apache 2.4.7
- PHP 5.5.9
- Basic knowledge of debugging with `strace`
- Understanding of Puppet manifests

## Problem Description

When attempting to access the WordPress site, Apache returns a `500 Internal Server Error`. This error is often due to a server-side issue, which requires debugging at the system level.

## Debugging Process

### Step 1: Use `strace` to Identify the Issue

To diagnose the problem, we used `strace`, a powerful diagnostic, debugging, and instructional tool for tracing system calls and signals.

```bash
strace -p $(pgrep -f apache2)
```

This command attaches `strace` to the running Apache process. By analyzing the output, we identified that the error was caused by a typo in the `wp-settings.php` file, where the `phpp` extension was mistakenly used instead of `php`.

### Step 2: Verify the Issue

To confirm the issue, we inspected the `wp-settings.php` file:

```bash
grep -i 'phpp' /var/www/html/wp-settings.php
```

### Step 3: Fix the Issue Manually

Initially, the issue was fixed manually by running the following command:

```bash
sed -i 's/phpp/php/g' /var/www/html/wp-settings.php
```

However, to ensure this fix is persistent and can be applied automatically, we used Puppet.

## Solution: Automate the Fix with Puppet

To automate the fix, we created a Puppet manifest `0-strace_is_your_friend.pp`. This manifest uses the `exec` resource to run the `sed` command, replacing any incorrect `phpp` extensions with `php`.

### Puppet Manifest: `0-strace_is_your_friend.pp`

```puppet
# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
```

### How It Works

- **Exec Resource**
The `exec` resource in Puppet allows you to execute arbitrary shell commands.
- **Command**: The `sed` command is used to search for occurrences of `phpp` and replace them with `php`.
- **Path**: Specifies the directories to search for executables when running the command.

### Step 4: Apply the Puppet Manifest

To apply the Puppet manifest and fix the issue automatically, run:

```bash
puppet apply 0-strace_is_your_friend.pp
```

### Step 5: Verify the Fix

Finally, verify that the fix has been applied successfully by checking the status of the WordPress site:

```bash
curl -sI http://127.0.0.1 | grep "200 OK"
```

If the `200 OK` response is returned, the issue has been resolved.

## Conclusion

By leveraging `strace` and Puppet, we successfully diagnosed and fixed a critical issue in the WordPress site. This solution not only resolved the immediate problem but also provided a way to automate the fix, ensuring the site remains stable in the future.

---
