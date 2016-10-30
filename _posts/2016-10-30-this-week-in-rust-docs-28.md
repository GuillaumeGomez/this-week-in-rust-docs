---
layout: post
title: This Week in Rust Docs 28
date: 2016-10-30
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

* [@joshtriplett](https://github.com/joshtriplett) copied/edited [on documentation for write! and writeln!](https://github.com/rust-lang/rust/pull/37473) and documented [convention for using both fmt::Write and io::Write](https://github.com/rust-lang/rust/pull/37472).
* [@AndiDog](https://github.com/AndiDog) added [E0532 error explanation](https://github.com/rust-lang/rust/pull/37475).
* [@liigo](https://github.com/liigo) added an [unsafe sign for unsafe functions in module page with superscript icons](https://github.com/rust-lang/rust/pull/37250).
* [@achanda](https://github.com/achanda) clarified [that send_to might panic in certain cases](https://github.com/rust-lang/rust/pull/37432).
* [@Cobrand](https://github.com/Cobrand) improved [docs for Index and IndexMut](https://github.com/rust-lang/rust/pull/37438).
* [@polo-language](https://github.com/polo-language) added [error note to illegal code snippet](https://github.com/rust-lang/rust/pull/37425).
* [@jfirebaugh](https://github.com/jfirebaugh) removed [long diagnostic for E0002](https://github.com/rust-lang/rust/pull/37058) and added [a distinct error code and description for "main function has wrong type"](https://github.com/rust-lang/rust/pull/37242).
* [@mikhail-m1](https://github.com/mikhail-m1) improved ["Doesn't live long enough" error](https://github.com/rust-lang/rust/pull/37405).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@brson](https://github.com/brson) removed [all "consider using an explicit lifetime parameter" suggestions](https://github.com/rust-lang/rust/pull/37057) and added [release notes for 1.12.1](https://github.com/rust-lang/rust/pull/37317).
* [@ollie27](https://github.com/ollie27) fixed [a few links in the docs](https://github.com/rust-lang/rust/pull/37316).
* [@phungleson](https://github.com/phungleson) updated [E0072 bonus to new error format](https://github.com/rust-lang/rust/pull/36466).
* [@johnthagen](https://github.com/johnthagen) added [example using Self to reference](https://github.com/rust-lang/rust/pull/37386).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) started [the implementation of proposal for E0308](https://github.com/rust-lang/rust/pull/37388), improved [reference cast help message](https://github.com/rust-lang/rust/pull/37375), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and printed [more tags in rustdoc](https://github.com/rust-lang/rust/pull/37134).

# Recent doc contributions

* [@bluss](https://github.com/bluss) added [documentation for Read, Write impls for slices and Vec](https://github.com/rust-lang/rust/pull/37343).
* [@loggerhead](https://github.com/loggerhead) fixed [an error of 'book/deref-coercions.html'](https://github.com/rust-lang/rust/pull/37228).
* [@mcarton](https://github.com/mcarton) fixed [bad error message with `::<` in types](https://github.com/rust-lang/rust/pull/36206).
* [@robinst](https://github.com/robinst) added [semicolon to "Maybe a missing `extern crate foo`" message](https://github.com/rust-lang/rust/pull/37430).
* [@zoffixznet](https://github.com/zoffixznet) fixed [typo](https://github.com/rust-lang/rust/pull/37398).
* [@mikhail-m1](https://github.com/mikhail-m1) made [error E0221 more helpful](https://github.com/rust-lang/rust/pull/37396).
* [@vtduncan](https://github.com/vtduncan) fixed [broken links in Vec docs](https://github.com/rust-lang/rust/pull/37391) and added [link to PathBuf from the Path docs](https://github.com/rust-lang/rust/pull/37372).
* [@typelist](https://github.com/typelist) fixed [typo that resulted in comparison-to-self](https://github.com/rust-lang/rust/pull/37358).
* [@aidanhs](https://github.com/aidanhs) `as_bytes` [is not the iterator on String, `bytes` is](https://github.com/rust-lang/rust/pull/37327).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [E0277 help message](https://github.com/rust-lang/rust/pull/37324) and added [missing urls in collections module](https://github.com/rust-lang/rust/pull/37304).

# Meetings

Next meeting will be on Wednesday 2nd of November 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
