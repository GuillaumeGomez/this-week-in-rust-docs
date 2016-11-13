---
layout: post
title: This Week in Rust Docs 30
date: 2016-11-13
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

* [@estebank](https://github.com/estebank) added [the detection for missing `;` on methods with return type `()`](https://github.com/rust-lang/rust/pull/36409), provided [hint when cast needs a dereference](https://github.com/rust-lang/rust/pull/37442), added [multiline spans in full if short enough](https://github.com/rust-lang/rust/pull/37369), disallowed ['start' feature on nested function in E0526](https://github.com/rust-lang/rust/pull/37548) and added the [detection for double reference when applying binary op](https://github.com/rust-lang/rust/pull/34420).
* [@keeperofdakeys](https://github.com/keeperofdakeys) improved [the #[should_panic] feature](https://github.com/rust-lang/rust/pull/37749).
* [@jedireza](https://github.com/jedireza) fixed [grammar typos in ffi.md](https://github.com/rust-lang/rust/pull/37743).
* [@brson](https://github.com/brson) removed [all "consider using an explicit lifetime parameter" suggestions](https://github.com/rust-lang/rust/pull/37057).
* [@jfirebaugh](https://github.com/jfirebaugh) removed [long diagnostic for E0002](https://github.com/rust-lang/rust/pull/37058) and added [a distinct error code and description for "main function has wrong type"](https://github.com/rust-lang/rust/pull/37242).
* [@dns2utf8](https://github.com/dns2utf8) added [grammar verification build command](https://github.com/rust-lang/rust/pull/37607).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [ref suggestion](https://github.com/rust-lang/rust/pull/37658), improved [reference cast help message](https://github.com/rust-lang/rust/pull/37375), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and started [implementation of proposal for E0308](https://github.com/rust-lang/rust/pull/37388).

# Recent doc contributions

* [@johnthagen](https://github.com/johnthagen) added [example using Self to reference](https://github.com/rust-lang/rust/pull/37386).
* [@brson](https://github.com/brson) added [changelog for 1.13.0](https://github.com/rust-lang/rust/pull/37600) and removed [platform compatibility table from the Book, link to the forge](https://github.com/rust-lang/rust/pull/37601).
* [@estebank](https://github.com/estebank) fixed [invalid "ref mut mut" sugestion](https://github.com/rust-lang/rust/pull/37531), included [type of missing trait methods in error](https://github.com/rust-lang/rust/pull/37370), added [note "how to escape" on fmt string with unescaped `{`](https://github.com/rust-lang/rust/pull/37695), removed [hint to add lifetime on impl items](https://github.com/rust-lang/rust/pull/37481), grouped [unused import warnings per import list](https://github.com/rust-lang/rust/pull/37456), showed [one error for duplicated type definitions](https://github.com/rust-lang/rust/pull/37447), pointed [to type argument span when used as trait](https://github.com/rust-lang/rust/pull/37428) and reworded [error when data-less enum variant called as function](https://github.com/rust-lang/rust/pull/36520).
* [@mikhail-m1](https://github.com/mikhail-m1) improved ["Doesn't live long enough" error](https://github.com/rust-lang/rust/pull/37554).
* [@liigo](https://github.com/liigo) [marked unsafe fns in module page with superscript icons in rustdoc](https://github.com/rust-lang/rust/pull/37250).
* [@xfix](https://github.com/xfix) matched [guessing game output to newest language version](https://github.com/rust-lang/rust/pull/37483).
* [@steveklabnik](https://github.com/steveklabnik) made [it clear that the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@joshtriplett](https://github.com/joshtriplett) documented [convention for using both fmt::Write and io::Write](https://github.com/rust-lang/rust/pull/37472).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) folded [fields for enum struct variants into a docblock in rustdoc](https://github.com/rust-lang/rust/pull/37728) and [added line breaks to where clauses a la rustfmt in rustdoc](https://github.com/rust-lang/rust/pull/37190).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) added [Error implementation for std::sync::mpsc::RecvTimeoutError.](https://github.com/rust-lang/rust/pull/37527).
* [@wesleywiser](https://github.com/wesleywiser) added [documentation to some of the unstable intrinsics](https://github.com/rust-lang/rust/pull/37662).
* [@nwin](https://github.com/nwin) removed [remark about poor code style](https://github.com/rust-lang/rust/pull/37503).
* [@trotter](https://github.com/trotter) updated [testing.md to reflect changes to cargo new](https://github.com/rust-lang/rust/pull/37368).
* [@tshepang](https://github.com/tshepang) fixed [doc typo](https://github.com/rust-lang/rust/pull/37680).
* [@est31](https://github.com/est31) documented [the question mark operator in reference and the Book's syntax index](https://github.com/rust-lang/rust/pull/37664).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls on io structs](https://github.com/rust-lang/rust/pull/37588), printed [more tags in rustdoc](https://github.com/rust-lang/rust/pull/37134), added [missing urls for FusedIterator and TrustedLen traits](https://github.com/rust-lang/rust/pull/37669), added [missing urls for marker's traits](https://github.com/rust-lang/rust/pull/37698), added [missing mem urls](https://github.com/rust-lang/rust/pull/37716), fixed [invalid src url](https://github.com/rust-lang/rust/pull/37727), added [missing urls and made few local rewrites](https://github.com/rust-lang/rust/pull/37627) and added [missing urls for Sum and Product traits](https://github.com/rust-lang/rust/pull/37650).

# Meetings

Next meeting will be on Wednesday 16th of November 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
