---
layout: post
title: This Week in Rust Docs 27
date: 2016-10-23
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

The ["new" run button](https://github.com/rust-lang/rust/pull/36334) has been merged and is now used in [nightly docs](https://doc.rust-lang.org/nightly/std/). Give it a try!

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

* [@bluss](https://github.com/bluss) added [documentation for Read, Write impls for slices and Vec](https://github.com/rust-lang/rust/pull/37343).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@brson](https://github.com/brson) added [release notes for 1.12.1](https://github.com/rust-lang/rust/pull/37317) and removed [all "consider using an explicit lifetime parameter" suggestions](https://github.com/rust-lang/rust/pull/37057).
* [@ollie27](https://github.com/ollie27) fixed [a few links in the docs](https://github.com/rust-lang/rust/pull/37316).
* [@liigo](https://github.com/liigo) is working on rustdoc: [flag unsafe fns in module's function list](https://github.com/rust-lang/rust/pull/37250).
* [@phungleson](https://github.com/phungleson) updated [E0072 bonus to new error format](https://github.com/rust-lang/rust/pull/36466).
* [@jfirebaugh](https://github.com/jfirebaugh) added [a distinct error code and description for "main function has wrong type"](https://github.com/rust-lang/rust/pull/37242) and removed [long diagnostic for E0002](https://github.com/rust-lang/rust/pull/37058).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) rustdoc: [add line breaks to where clauses a la rustfmt](https://github.com/rust-lang/rust/pull/37190).
* [@loggerhead](https://github.com/loggerhead) fixed [an error of 'book/deref-coercions.html'](https://github.com/rust-lang/rust/pull/37228).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@diwic](https://github.com/diwic) fixed [documentation typo](https://github.com/rust-lang/rust/pull/36849).* [@GuillaumeGomez](https://github.com/GuillaumeGomez) Improve [E0277 help message](https://github.com/rust-lang/rust/pull/37324), Add [missing urls in collections module](https://github.com/rust-lang/rust/pull/37304), Add [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and Print [more tags in rustdoc](https://github.com/rust-lang/rust/pull/37134).


# Recent doc contributions

* [@frewsxcv](https://github.com/frewsxcv) improved [doc example for `std::borrow::Cow`](https://github.com/rust-lang/rust/pull/37187).
* [@nabeelomer](https://github.com/nabeelomer) updated [the docs for Error::description](https://github.com/rust-lang/rust/pull/37189).
* [@aidanhs](https://github.com/aidanhs) `as_bytes` [is not the iterator on String, `bytes` is](https://github.com/rust-lang/rust/pull/37327).
* [@tshepang](https://github.com/tshepang) added [a simpler description of Iterator::nth](https://github.com/rust-lang/rust/pull/37314).
* [@vkatsikaros](https://github.com/vkatsikaros) made [a minor clarification in guessing game](https://github.com/rust-lang/rust/pull/37309).
* [@senior](https://github.com/senior) added [error explaination for E0182, E0230 and E0399](https://github.com/rust-lang/rust/pull/37244).
* [@mikhail-m1](https://github.com/mikhail-m1) improved ["Doesn't live long enough" error](https://github.com/rust-lang/rust/pull/37174).
* [@ollie27](https://github.com/ollie27) rustdoc: [Improve playground run buttons](https://github.com/rust-lang/rust/pull/37098).
* [@zackmdavis](https://github.com/zackmdavis) corrected [erroneous pluralization of '1 type argument' error messages](https://github.com/rust-lang/rust/pull/37193).
* [@jethrogb](https://github.com/jethrogb) added [stable example to TypeId](https://github.com/rust-lang/rust/pull/37240).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls for io types](https://github.com/rust-lang/rust/pull/37165), added [invalid doc comment help message](https://github.com/rust-lang/rust/pull/36964), added [missing urls on Vec docs](https://github.com/rust-lang/rust/pull/37043), Rollup [of 10 pull requests](https://github.com/rust-lang/rust/pull/37337), Rollup [of 7 pull requests](https://github.com/rust-lang/rust/pull/37289), Add [more io urls](https://github.com/rust-lang/rust/pull/37259) and Rollup [of 6 pull requests](https://github.com/rust-lang/rust/pull/37237).

# Meetings

Next meeting will be on Wednesday 26th of October 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
