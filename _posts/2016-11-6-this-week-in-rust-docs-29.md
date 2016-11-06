---
layout: post
title: This Week in Rust Docs 29
date: 2016-11-6
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

* [@johnthagen](https://github.com/johnthagen) added [example using Self to reference](https://github.com/rust-lang/rust/pull/37386).
* [@brson](https://github.com/brson) added [changelog for 1.13.0](https://github.com/rust-lang/rust/pull/37600), and removed [all "consider using an explicit lifetime parameter" suggestions](https://github.com/rust-lang/rust/pull/37057).
* [@estebank](https://github.com/estebank) fixed [invalid "ref mut mut" sugestion](https://github.com/rust-lang/rust/pull/37531) and provided [hint when cast needs a dereference](https://github.com/rust-lang/rust/pull/37442).
* [@mikhail-m1](https://github.com/mikhail-m1) improved ["Doesn't live long enough" error](https://github.com/rust-lang/rust/pull/37554).
* [@liigo](https://github.com/liigo) [marked unsafe fns in module page with superscript icons in rustdoc](https://github.com/rust-lang/rust/pull/37250).
* [@xfix](https://github.com/xfix) matched [guessing game output to newest language version](https://github.com/rust-lang/rust/pull/37483).
* [@steveklabnik](https://github.com/steveklabnik) made [it clear that the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@joshtriplett](https://github.com/joshtriplett) documented [convention for using both fmt::Write and io::Write](https://github.com/rust-lang/rust/pull/37472).
* [@jfirebaugh](https://github.com/jfirebaugh) removed [long diagnostic for E0002](https://github.com/rust-lang/rust/pull/37058) and added [a distinct error code and description for "main function has wrong type"](https://github.com/rust-lang/rust/pull/37242).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls on io structs](https://github.com/rust-lang/rust/pull/37588), started [implementation of proposal for E0308](https://github.com/rust-lang/rust/pull/37388), improved [reference cast help message](https://github.com/rust-lang/rust/pull/37375) and printed [more tags in rustdoc](https://github.com/rust-lang/rust/pull/37134).

# Recent doc contributions

* [@joshtriplett](https://github.com/joshtriplett) copied/edited [on documentation for write! and writeln!](https://github.com/rust-lang/rust/pull/37473).
* [@AndiDog](https://github.com/AndiDog) added [E0532 error explanation](https://github.com/rust-lang/rust/pull/37475).
* [@Cobrand](https://github.com/Cobrand) improved [docs for Index and IndexMut](https://github.com/rust-lang/rust/pull/37438).
* [@mikhail-m1](https://github.com/mikhail-m1) improved ["Doesn't live long enough" error](https://github.com/rust-lang/rust/pull/37405).
* [@ollie27](https://github.com/ollie27) fixed [a few links in the docs](https://github.com/rust-lang/rust/pull/37316).
* [@d-unseductable](https://github.com/d-unseductable) elided [lifetimes in DerefMut documentation](https://github.com/rust-lang/rust/pull/37523).
* [@pfrenssen](https://github.com/pfrenssen) updated ["Testing" chapter for 1.12](https://github.com/rust-lang/rust/pull/37484).
* [@xfix](https://github.com/xfix) removed [mention of "*" dependency version in guessing game example](https://github.com/rust-lang/rust/pull/37485).
* [@diwic](https://github.com/diwic) fixed [str documentation typo](https://github.com/rust-lang/rust/pull/36849).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls for ErrorKind's variants](https://github.com/rust-lang/rust/pull/37537).

# Meetings

Next meeting will be on Wednesday 9th of November 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
