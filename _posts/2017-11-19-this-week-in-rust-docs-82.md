---
layout: post
title: This Week in Rust Docs 82
date: 2017-11-19
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

The switch to [Pulldown](https://github.com/google/pulldown-cmark) for the rust doc rendering has finally [started](https://github.com/rust-lang/rust/pull/41991)!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781) and showed in docs [whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039).
* [@Aaronepower](https://github.com/Aaronepower) updated [Release notes for 1.22.0](https://github.com/rust-lang/rust/pull/45454).
* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45776), accounted [for missing keyword in fn/struct definition](https://github.com/rust-lang/rust/pull/45997), used [the proper term when using non-existing variant](https://github.com/rust-lang/rust/pull/46024), used [multiline text for crate conflict diagnostics](https://github.com/rust-lang/rust/pull/45946), displayed [`\t` in diagnostics code as four spaces](https://github.com/rust-lang/rust/pull/45953), highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752) and removed [dereference suggestion on tuple argument](https://github.com/rust-lang/rust/pull/45947).
* [@fhartwig](https://github.com/fhartwig) made [rustdoc not include self-by-value methods from Deref target](https://github.com/rust-lang/rust/pull/45645).
* [@JRegimbal](https://github.com/JRegimbal) changed ["Types/modules" title of search tab to be more accurate](https://github.com/rust-lang/rust/pull/45898).
* [@oli-obk](https://github.com/oli-obk) added [structured suggestions for various "use" suggestions](https://github.com/rust-lang/rust/pull/46035) and included [rendered diagnostic in json](https://github.com/rust-lang/rust/pull/46052).
* [@sinkuu](https://github.com/sinkuu) added [doc for doing `Read` from `&str`](https://github.com/rust-lang/rust/pull/46088).
* [@kennytm](https://github.com/kennytm) combined ["this expression will panic at run-time" warnings into `const_err` lint](https://github.com/rust-lang/rust/pull/46049).
* [@ollie27](https://github.com/ollie27) fixed [broken CSS for book redirect pages](https://github.com/rust-lang/rust/pull/45998).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [path search](https://github.com/rust-lang/rust/pull/46081).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [talk about #![doc(test(no_crate_inject))] and #![doc(test(attr(...)))] in rustdoc](https://github.com/rust-lang/rust/pull/45767), tweaked [notes on ignore/compile_fail examples in rustdoc](https://github.com/rust-lang/rust/pull/45815) and updated examples: [in Cow::into_owned don't need to wrap result in Cows](https://github.com/rust-lang/rust/pull/45993).
* [@steveklabnik](https://github.com/steveklabnik) started [shipping the Cargo book](https://github.com/rust-lang/rust/pull/45692).
* [@pornel](https://github.com/pornel) removed [deprecated message](https://github.com/rust-lang/rust/pull/45828).
* [@oli-obk](https://github.com/oli-obk) removed [left over dead code from suggestion diagnostic refactoring](https://github.com/rust-lang/rust/pull/46039).
* [@kennytm](https://github.com/kennytm) fixed [several pulldown warnings when documenting libstd](https://github.com/rust-lang/rust/pull/45977).
* [@lnicola](https://github.com/lnicola) escaped [doc root URLs in rustdoc](https://github.com/rust-lang/rust/pull/46010).
* [@ExpHP](https://github.com/ExpHP) added [context to E0084, E0517, E0518](https://github.com/rust-lang/rust/pull/45984).
* [@zackmdavis](https://github.com/zackmdavis) deduplicated [projection error (E0271) messages](https://github.com/rust-lang/rust/pull/45952).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [search over generic types in docs](https://github.com/rust-lang/rust/pull/45673), fixed [primitive types not showing up](https://github.com/rust-lang/rust/pull/46066), set [short-message feature unstable](https://github.com/rust-lang/rust/pull/46005) and added [missing links in FromStr docs](https://github.com/rust-lang/rust/pull/45970).

# Meetings

Next meeting will be on Tuesday 21st of November 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
