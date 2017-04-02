---
layout: post
title: This Week in Rust Docs 50
date: 2017-4-2
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

The markdown renderer in rustdoc [has been changed](https://github.com/rust-lang/rust/pull/40338)! We replaced [hoedown](https://github.com/hoedown/hoedown) with [pulldown-cmark](https://github.com/google/pulldown-cmark). Bugs might appear after this switch so any feedback is very welcomed! An issue has been opened [here](https://github.com/rust-lang/rust/issues/40912).

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) suggested [using enum when a variant is used as a type](https://github.com/rust-lang/rust/pull/40775), pointed [to definition when modifying field of immutable variable](https://github.com/rust-lang/rust/pull/40767), pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857) and added [an explicit help message for binop type mismatch](https://github.com/rust-lang/rust/pull/40565).
* [@mandeep](https://github.com/mandeep) fixed [typo in doc comments for swap_remove](https://github.com/rust-lang/rust/pull/41019).
* [@frewsxcv](https://github.com/frewsxcv) made a [couple minor improvements for tidy error handling](https://github.com/rust-lang/rust/pull/40653).
* [@stjepang](https://github.com/stjepang) added [a note about overflow for fetch_add/fetch_sub](https://github.com/rust-lang/rust/pull/40927) and improved [some docs for VecDeque](https://github.com/rust-lang/rust/pull/40949).
* [@irfanhudda](https://github.com/irfanhudda) improved [option API docs](https://github.com/rust-lang/rust/pull/40999) and improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@SimonSapin](https://github.com/SimonSapin) fixed [link to current() in std::thread docs](https://github.com/rust-lang/rust/pull/41014).
* [@pgerber](https://github.com/pgerber) improved [documentation for `std::fs::DirBuilder`](https://github.com/rust-lang/rust/pull/41007).
* [@sagebind](https://github.com/sagebind) improved [examples for ThreadId](https://github.com/rust-lang/rust/pull/41008).
* [@stepancheg](https://github.com/stepancheg) improved [BufRead::is_eof documentation](https://github.com/rust-lang/rust/pull/40747).
* [@maccoda](https://github.com/maccoda) improved [Convert docs](https://github.com/rust-lang/rust/pull/40987).
* [@donniebishop](https://github.com/donniebishop) added [links to types in from_utf8 description](https://github.com/rust-lang/rust/pull/40997) and added [links to from_utf8 methods in Utf8Error](https://github.com/rust-lang/rust/pull/40992).
* [@Technius](https://github.com/Technius) added [links and some examples to std::sync::mpsc docs](https://github.com/rust-lang/rust/pull/40981).
* [@mgattozzi](https://github.com/mgattozzi) updated [`Child` docs to not have a note section](https://github.com/rust-lang/rust/pull/40812) and updated [ChildStderr docs to be clearer](https://github.com/rust-lang/rust/pull/40829).
* [@projektir](https://github.com/projektir) updated [the description for BarrierWaitResult](https://github.com/rust-lang/rust/pull/40977).
* [@pirate](https://github.com/pirate) added [contribution instructions to stdlib docs](https://github.com/rust-lang/rust/pull/40765).
* [@tschottdorf](https://github.com/tschottdorf) improved [error when violating `for<'a> T: 'a`](https://github.com/rust-lang/rust/pull/40413).
* [@GAJaloyan](https://github.com/GAJaloyan) fixed [mistakes in the README.md file](https://github.com/rust-lang/rust/pull/40797).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [ref suggestion](https://github.com/rust-lang/rust/pull/37658), added [support for image, rules and footnotes in the new rustdoc markdown renderer](https://github.com/rust-lang/rust/pull/40919), fixed [mutex's docs inconsistency](https://github.com/rust-lang/rust/pull/40608) and added [more explanation on RefCell::get_mut](https://github.com/rust-lang/rust/pull/40634).

# Recent doc contributions

* [@projektir](https://github.com/projektir) added [linking for Once docs](https://github.com/rust-lang/rust/pull/40866), added [links for Atomics docs](https://github.com/rust-lang/rust/pull/40871) and updated [rustdoc to accept `#` at the start of a markdown file](https://github.com/rust-lang/rust/pull/40828).
* [@donniebishop](https://github.com/donniebishop) modified [`str` structs descriptions](https://github.com/rust-lang/rust/pull/40935), linked [str in from_utf_unchecked](https://github.com/rust-lang/rust/pull/40907), added [a `fromStr` implementation example](https://github.com/rust-lang/rust/pull/40824) and linked [ParseBoolError to from_str method of bool](https://github.com/rust-lang/rust/pull/40819).
* [@frewsxcv](https://github.com/frewsxcv) synced [all unstable features with Unstable Book; add tidy lint.](https://github.com/rust-lang/rust/pull/40694) and added [all unstable features to Unstable Book.](https://github.com/rust-lang/rust/pull/40786).
* [@pirate](https://github.com/pirate) added [helpful hint in io docs about how ? is not allowed in main()](https://github.com/rust-lang/rust/pull/40763).
* [@topecongiro](https://github.com/topecongiro) made [overlapping_inherent_impls lint a hard error](https://github.com/rust-lang/rust/pull/40728).
* [@MaloJaffre](https://github.com/MaloJaffre) removed [unused feature from error index generator](https://github.com/rust-lang/rust/pull/40898) and avoid [linking to a moved page in rust.html](https://github.com/rust-lang/rust/pull/40901).
* [@SamWhited](https://github.com/SamWhited) improved [the docs for the write and writeln macros](https://github.com/rust-lang/rust/pull/40934).
* [@DaseinPhaos](https://github.com/DaseinPhaos) added [missing link in unstable-book](https://github.com/rust-lang/rust/pull/40925).
* [@rap2hpoutre](https://github.com/rap2hpoutre) added[example to std::process::abort](https://github.com/rust-lang/rust/pull/40904).
* [@wesleywiser](https://github.com/wesleywiser) made [the rustdoc sidebar white on `src` pages](https://github.com/rust-lang/rust/pull/40888).
* [@ctjhoa](https://github.com/ctjhoa) improved [os::linux documentation](https://github.com/rust-lang/rust/pull/40869).
* [@abonander](https://github.com/abonander) memorized [`pub use`-reexported macros so they don't appear twice in docs](https://github.com/rust-lang/rust/pull/40814).
* [@estebank](https://github.com/estebank) clarified [suggetion for field used as method](https://github.com/rust-lang/rust/pull/40816).
* [@irfanhudda](https://github.com/irfanhudda) fixed [typo in libcore/char.rs](https://github.com/rust-lang/rust/pull/40897).
* [@steveklabnik](https://github.com/steveklabnik) updated [various book modules](https://github.com/rust-lang/rust/pull/40864).
* [@lukaramu](https://github.com/lukaramu) improved [std::net docs](https://github.com/rust-lang/rust/pull/40838).
* [@stepancheg](https://github.com/stepancheg) documented [Cursor::new position is 0](https://github.com/rust-lang/rust/pull/40783).
* [@TigleyM](https://github.com/TigleyM) updated [docs for std::str](https://github.com/rust-lang/rust/pull/40682).
* [@ollie27](https://github.com/ollie27) fixed [broken Markdown and bad links in the error index](https://github.com/rust-lang/rust/pull/40853) and fixed [compiler docs again](https://github.com/rust-lang/rust/pull/40852).
* [@alanstoate](https://github.com/alanstoate) changed [string references in asciiext](https://github.com/rust-lang/rust/pull/40837).
* [@Wallacoloo](https://github.com/Wallacoloo) fixed [typo in char::to_uppercase documentation](https://github.com/rust-lang/rust/pull/40833).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) replaced [hoedown with pulldown in rustdoc](https://github.com/rust-lang/rust/pull/40338), replaced [hoedown with pull in rustdoc](https://github.com/rust-lang/rust/pull/40338) and added [missing urls in ptr docs](https://github.com/rust-lang/rust/pull/40703).

# Meetings

Next meeting will be on Wednesday 5th of April 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
