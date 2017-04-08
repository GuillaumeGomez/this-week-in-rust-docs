---
layout: post
title: This Week in Rust Docs 51
date: 2017-4-9
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

The markdown renderer in rustdoc [has been changed](https://github.com/rust-lang/rust/pull/40338)! We replaced [hoedown](https://github.com/hoedown/hoedown) with [pulldown-cmark](https://github.com/google/pulldown-cmark). Bugs might appear after this switch so any feedback is very welcomed!

However, thanks to everyone's efforts, all known issues have been fixed. Don't forget to check if your document is common-mark compliant!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) updated [formatting of fn signatures and where clauses to match style rfcs in rustdoc](https://github.com/rust-lang/rust/pull/41084).
* [@estebank](https://github.com/estebank) pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857), added [an explicit help message for binop type mismatch](https://github.com/rust-lang/rust/pull/40565), added [end line display of multiline annotations](https://github.com/rust-lang/rust/pull/41136) and used [proper span for tuple index parsed as float](https://github.com/rust-lang/rust/pull/41087).
* [@frewsxcv](https://github.com/frewsxcv) made a [couple minor improvements for tidy error handling](https://github.com/rust-lang/rust/pull/40653).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@sagebind](https://github.com/sagebind) improved [examples for ThreadId](https://github.com/rust-lang/rust/pull/41008).
* [@stepancheg](https://github.com/stepancheg) improved [BufRead::is_eof documentation](https://github.com/rust-lang/rust/pull/40747).
* [@maccoda](https://github.com/maccoda) improved [Convert docs](https://github.com/rust-lang/rust/pull/40987).
* [@mgattozzi](https://github.com/mgattozzi) updated [`Child` docs to not have a note section](https://github.com/rust-lang/rust/pull/40812) and updated [ChildStderr docs to be clearer](https://github.com/rust-lang/rust/pull/40829).
* [@pirate](https://github.com/pirate) added [contribution instructions to stdlib docs](https://github.com/rust-lang/rust/pull/40765).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@projektir](https://github.com/projektir) added [channel error docs](https://github.com/rust-lang/rust/pull/41103).
* [@lukaramu](https://github.com/lukaramu) improved [std::hash docs](https://github.com/rust-lang/rust/pull/41125).
* [@palango](https://github.com/palango) improved [module documentation for std::f32 and std::f64](https://github.com/rust-lang/rust/pull/41122).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and added [more explanation on RefCell::get_mut](https://github.com/rust-lang/rust/pull/40634).

# Recent doc contributions

* [@ollie27](https://github.com/ollie27) fixed [Markdown issues in the docs](https://github.com/rust-lang/rust/pull/41111) and used [pulldown-cmark for Markdown HTML rendering in rustdox](https://github.com/rust-lang/rust/pull/41112).
* [@estebank](https://github.com/estebank) suggested [using enum when a variant is used as a type](https://github.com/rust-lang/rust/pull/40775), identified [missing item category in `impl`s](https://github.com/rust-lang/rust/pull/40815) and removed [recommendations of private fields called as method](https://github.com/rust-lang/rust/pull/41062).
* [@mandeep](https://github.com/mandeep) fixed [typo in doc comments for swap_remove](https://github.com/rust-lang/rust/pull/41019).
* [@stjepang](https://github.com/stjepang) added [a note about overflow for fetch_add/fetch_sub](https://github.com/rust-lang/rust/pull/40927) and improved [some docs for VecDeque](https://github.com/rust-lang/rust/pull/40949).
* [@irfanhudda](https://github.com/irfanhudda) improved [option API docs](https://github.com/rust-lang/rust/pull/40999).
* [@SimonSapin](https://github.com/SimonSapin) fixed [link in std::thread docs](https://github.com/rust-lang/rust/pull/41014).
* [@pgerber](https://github.com/pgerber) improved [documentation for `std::fs::DirBuilder`](https://github.com/rust-lang/rust/pull/41007).
* [@donniebishop](https://github.com/donniebishop) added [links to types in from_utf8 description](https://github.com/rust-lang/rust/pull/40997) and added [links to from_utf8 methods in Utf8Error](https://github.com/rust-lang/rust/pull/40992).
* [@Technius](https://github.com/Technius) added [links and some examples to std::sync::mpsc docs](https://github.com/rust-lang/rust/pull/40981).
* [@projektir](https://github.com/projektir) updated [the description for BarrierWaitResult](https://github.com/rust-lang/rust/pull/40977).
* [@GAJaloyan](https://github.com/GAJaloyan) fixed [mistakes in the README.md file](https://github.com/rust-lang/rust/pull/40797).
* [@japaric](https://github.com/japaric) documented [some existing unstable features](https://github.com/rust-lang/rust/pull/41135).
* [@euclio](https://github.com/euclio) collapsed [docblock before showing label in rustdoc](https://github.com/rust-lang/rust/pull/41131).
* [@rap2hpoutre](https://github.com/rap2hpoutre) added [example to std::process::abort](https://github.com/rust-lang/rust/pull/41090).
* [@steveklabnik](https://github.com/steveklabnik) fixed [links](https://github.com/rust-lang/rust/pull/41066).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [support for image, rules and footnotes in the new rustdoc markdown renderer](https://github.com/rust-lang/rust/pull/40919), fixed [mutex's docs inconsistency](https://github.com/rust-lang/rust/pull/40608) and replaced [`^` with `<sup>` html balise](https://github.com/rust-lang/rust/pull/41043).

# Meetings

Next meeting will be on Wednesday 12th of April 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
