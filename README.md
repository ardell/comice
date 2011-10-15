Comice (kuh-MEES)
=================
Comice makes it easy to create PEAR sandboxes and use the sandboxed code and CLI apps with your project without crying.

Inspired by bundler and rvm from the Ruby world.

Usage:
------
  exec
	  Execute a command scoped to the appropriate pear context.

	pear
	  Manage a PEAR sandbox without having to juggle paths or conf files.

	pear-init
	  Initialize a PEAR sandbox: comice pear-init [externals-dir location] [pearrc location]

Installation
------------
	pear channel-discover pearfarm.pearfarm.org
	pear install pearfarm/comice-alpha

Normal Usage
------------
    $ comice pear-init
    ...bootstraps a sandbox...

    $ comice pear install pkga pkgb
    ...installs...

	$ comice exec pkga foo bar
	...WIN!...

From your webapp:

	ini_set('include_path', '/path/to/externals/pear/php:' . ini_get('include_path'));


What is comice?
---------------
What the heck is a "comice"? Comice pears are the best pears in the world, made famous by Harry & David.