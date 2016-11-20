---
layout: post
title: This Week in Rust Docs 31
date: 2016-11-20
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

Since new rustc version is out, the controversial changes on docs have been merged:

 * Fold [fields for enum struct variants into a docblock in rustdoc](https://github.com/rust-lang/rust/pull/37728)
 * Add [line breaks to where clauses a la rustfmt in rustdoc](https://github.com/rust-lang/rust/pull/37190).
 * Print [more tags in rustdoc](https://github.com/rust-lang/rust/pull/37134).

Don't hesitate to give your feedbacks on them!


The way rustdoc is creating urls is problematic for the moment. A good summary of this issue can be found [here](https://github.com/rust-lang/rust/issues/36417). A few members of the Rust Doc team are preparing an RFC in order to improve this. If you want to get involved, feel free to speak about it with [Guillaume Gomez](https://github.com/GuillaumeGomez) (imperio on IRC).

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [Error code list which need to be updated to new format](https://github.com/rust-lang/rust/issues/35233)
* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@eddyb](https://github.com/eddyb) separated [test collection from the main "clean"-ing pipeline in rustdoc](https://github.com/rust-lang/rust/pull/37890).
* [@estebank](https://github.com/estebank) provided [hint when cast needs a dereference](https://github.com/rust-lang/rust/pull/37442).
* [@birkenfeld](https://github.com/birkenfeld) fixed [duplicate bullet points in feature list](https://github.com/rust-lang/rust/pull/37876).
* [@brcooley](https://github.com/brcooley) fixed [grammar error in lifetimes.md](https://github.com/rust-lang/rust/pull/37840).
* [@ojsheikh](https://github.com/ojsheikh) updated [E0088 to new error format](https://github.com/rust-lang/rust/pull/37835).
* [@steveklabnik](https://github.com/steveklabnik) clarified [the reference's status.](https://github.com/rust-lang/rust/pull/37836).
* [@jfirebaugh](https://github.com/jfirebaugh) added [a distinct error code and description for "main function has wrong type"](https://github.com/rust-lang/rust/pull/37242).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [unneeded tricky macro doc](https://github.com/rust-lang/rust/pull/37870), added [missing examples for Ipv6Addr](https://github.com/rust-lang/rust/pull/37859), added [missing examples in SocketAddr](https://github.com/rust-lang/rust/pull/37880), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and added [ref suggestion](https://github.com/rust-lang/rust/pull/37658).

# Recent doc contributions

* [@keeperofdakeys](https://github.com/keeperofdakeys) improved [the #[should_panic] feature(https://github.com/rust-lang/rust/pull/37749) and show [a better error when using --test with #[proc_macro_derive]](https://github.com/rust-lang/rust/pull/37826).
* [@jedireza](https://github.com/jedireza) fixed [grammar typos in ffi.md(https://github.com/rust-lang/rust/pull/37743).
* [@dns2utf8](https://github.com/dns2utf8) added [grammar verification build command(https://github.com/rust-lang/rust/pull/37607).
* [@liigo](https://github.com/liigo) added [cli argument `--playground-url` in rustdoc](https://github.com/rust-lang/rust/pull/37763).
* [@tshepang](https://github.com/tshepang) fixed [nits and typos on comments in doc](https://github.com/rust-lang/rust/pull/37821).
* [@robinst](https://github.com/robinst) added [semicolon to "perhaps add a `use` for one of them" help](https://github.com/rust-lang/rust/pull/37759).
* [@tarka](https://github.com/tarka) added [sections about testing concurrency and stdout/err capture](https://github.com/rust-lang/rust/pull/37766).
* [@ollie27](https://github.com/ollie27) fixed [some local inlining issues in rustdoc](https://github.com/rust-lang/rust/pull/37773).
* [@frewsxcv](https://github.com/frewsxcv) updated [top-level path doc examples to show results.](https://github.com/rust-lang/rust/pull/37774) and rewrote [`std::path::Path::push` doc example.](https://github.com/rust-lang/rust/pull/37754).
* [@euclio](https://github.com/euclio) removed [deprecated text for unstable docs](https://github.com/rust-lang/rust/pull/37758).
* [@polo-language](https://github.com/polo-language) improved [punctuation, capitalization, and sentence structure of code snippet comments](https://github.com/rust-lang/rust/pull/37755).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) folded [fields for enum struct variants into a docblock in rustdoc](https://github.com/rust-lang/rust/pull/37728).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [reference cast help message(https://github.com/rust-lang/rust/pull/37375), added [net examples](https://github.com/rust-lang/rust/pull/37806) and uncommented [some long error explanation](https://github.com/rust-lang/rust/pull/37757).

# Meetings

Next meeting will be on Wednesday 23rd of November 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
