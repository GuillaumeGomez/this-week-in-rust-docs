---
layout: post
title: This Week in Rust Docs 94
date: 2018-2-25
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](https://doc.rust-lang.org/beta/)
* [Nightly](https://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

Hoedown is finally being removed from rustdoc! I'll post the approval message from [@QuietMisdreavus](https://github.com/QuietMisdreavus) in here:

> The preparations are complete. It is time...
>
> _**Begone, demon of the foul C! Your presence is no longer wanted here! With this strike, I commit you to the depths of history, never to torment our fair land again!**_

You can see the pull request [here](https://github.com/rust-lang/rust/pull/48274).

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) reworded [E0044 and message for `!Send` types](https://github.com/rust-lang/rust/pull/48138), suggested [setting associated type when type argument is given instead](https://github.com/rust-lang/rust/pull/48288) and provided [context for missing comma in match arm and if statement without block](https://github.com/rust-lang/rust/pull/48338).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vi](https://github.com/vi) added [foldable impl blocks in rustdoc](https://github.com/rust-lang/rust/pull/47894).
* [@wesleywiser](https://github.com/wesleywiser) fixed [how paths are printed by error messages during bootstrap](https://github.com/rust-lang/rust/pull/47731).
* [@NovemberZulu](https://github.com/NovemberZulu) rephrased [UnsafeCell doc](https://github.com/rust-lang/rust/pull/48201).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [readme for librustdoc](https://github.com/rust-lang/rust/pull/48283).
* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@zilbuz](https://github.com/zilbuz) showed [the used type variable when issuing a "can't use type parameters from outer function" error message](https://github.com/rust-lang/rust/pull/47574).
* [@remexre](https://github.com/remexre) fixed [docs for ASCII functions to no longer claim U+0021 is '@'](https://github.com/rust-lang/rust/pull/48529).
* [@christianpoveda](https://github.com/christianpoveda) made [new Cell docs](https://github.com/rust-lang/rust/pull/48474).
* [@mark-i-m](https://github.com/mark-i-m) splitted [E0404 to E0909; get rid of E0245](https://github.com/rust-lang/rust/pull/48446) and started [moving to the rustc guide!](https://github.com/rust-lang/rust/pull/48479).
* [@frewsxcv](https://github.com/frewsxcv) clarified ["It is an error to..." wording for zero-duration behaviors](https://github.com/rust-lang/rust/pull/48328).
* [@Phlosioneer](https://github.com/Phlosioneer) made [slight modification to the as_ref example of std::option::Option](https://github.com/rust-lang/rust/pull/48509).
* [@Centril](https://github.com/Centril) documented [panics in Clone, PartialEq, PartialOrd, Ord for RefCell](https://github.com/rust-lang/rust/pull/48365).
* [@flip1995](https://github.com/flip1995) suggested [type for overflowing bin/hex-literals](https://github.com/rust-lang/rust/pull/48432).
* [@jethrogb](https://github.com/jethrogb) clarified [interfaction between File::set_len and file cursor](https://github.com/rust-lang/rust/pull/48480).
* [@lukaslueg](https://github.com/lukaslueg) fixed [spelling s/casted/cast/](https://github.com/rust-lang/rust/pull/48403).
* [@RalfJung](https://github.com/RalfJung) warned [about ignored generic bounds in `for`](https://github.com/rust-lang/rust/pull/48326).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.25.0](https://github.com/rust-lang/rust/pull/48374).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added back [rustc explain](https://github.com/rust-lang/rust/pull/48337), added [resource-suffix option for rustdoc](https://github.com/rust-lang/rust/pull/48511), add [root-path](https://github.com/rust-lang/rust/pull/48442), added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), added [new warning for CStr::from_ptr](https://github.com/rust-lang/rust/pull/48507), added [rustdoc theme securities](https://github.com/rust-lang/rust/pull/48381) and fixed [auto trait impl rustdoc ice](https://github.com/rust-lang/rust/pull/48473).

# Recent doc contributions

* [@estebank](https://github.com/estebank) avoided [ICE in arg mistmatch error for tuple variants](https://github.com/rust-lang/rust/pull/48246) and handled [custom diagnostic for `&str + String`](https://github.com/rust-lang/rust/pull/48392).
* [@Aaron1011](https://github.com/Aaron1011) generated [documentation for auto-trait impls](https://github.com/rust-lang/rust/pull/47833).
* [@topecongiro](https://github.com/topecongiro) fixed [span of visibility](https://github.com/rust-lang/rust/pull/47799).
* [@csmoe](https://github.com/csmoe) informed [user where to give a type annotation](https://github.com/rust-lang/rust/pull/48198).
* [@frewsxcv](https://github.com/frewsxcv) unified ['Platform-specific behavior' documentation headings](https://github.com/rust-lang/rust/pull/48312), fixed [broken documentation link](https://github.com/rust-lang/rust/pull/48314) and marked [doc examples w/ `extern` blocks as `ignore`](https://github.com/rust-lang/rust/pull/48325).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) moved [manual "extern crate" statements outside automatic "fn main"s in doctests in rustdoc](https://github.com/rust-lang/rust/pull/48106) and fixed [crash when an external trait's docs needs to import another trait in rustdoc](https://github.com/rust-lang/rust/pull/48415).
* [@alercah](https://github.com/alercah) added [a warning to File about mutability](https://github.com/rust-lang/rust/pull/48273).
* [@matthiaskrgr](https://github.com/matthiaskrgr) fixed [more typos found by codespell](https://github.com/rust-lang/rust/pull/48275).
* [@varkor](https://github.com/varkor) introduce [UnpackedKind](https://github.com/rust-lang/rust/pull/48452).
* [@Manishearth](https://github.com/Manishearth) implemented [implied shortcut links for intra-rustdoc-links](https://github.com/rust-lang/rust/pull/48335).
* [@dwijnand](https://github.com/dwijnand) fixed [capitalisation in Path#file_name's docs](https://github.com/rust-lang/rust/pull/48499).
* [@steveklabnik](https://github.com/steveklabnik) updated [the book to promote second edition](https://github.com/rust-lang/rust/pull/48404).
* [@withoutboats](https://github.com/withoutboats) added [nonstandard_style alias for bad_style](https://github.com/rust-lang/rust/pull/48386).
* [@mbrubeck](https://github.com/mbrubeck) made [minor wording changes to drain_filter docs](https://github.com/rust-lang/rust/pull/48438).
* [@adeschamps](https://github.com/adeschamps) made [a small grammar fix to docs for String::new()](https://github.com/rust-lang/rust/pull/48436).
* [@ordovicia](https://github.com/ordovicia) take [2^5 as examples in document of pow()](https://github.com/rust-lang/rust/pull/48397).
* [@redcape](https://github.com/redcape) fixed [count usize link typo in docs](https://github.com/rust-lang/rust/pull/48360).
* [@m0ppers](https://github.com/m0ppers) added [missing link for read_line](https://github.com/rust-lang/rust/pull/48354).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [hoedown from rustdoc](https://github.com/rust-lang/rust/pull/48274), added [doc test command](https://github.com/rust-lang/rust/pull/48194) and fixed [rustdoc test ICE](https://github.com/rust-lang/rust/pull/48382).

# Meetings

Next meeting will be on Tuesday 27th of February 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
