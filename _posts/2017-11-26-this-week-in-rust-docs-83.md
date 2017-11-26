---
layout: post
title: This Week in Rust Docs 83
date: 2017-11-26
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

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45776), accounted [for missing keyword in fn/struct definition](https://github.com/rust-lang/rust/pull/45997), displayed [`\t` in diagnostics code as four spaces](https://github.com/rust-lang/rust/pull/45953), highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), suggest3e [using slice when encountering `let x = ""[..];`](https://github.com/rust-lang/rust/pull/46249) and used [suggestions instead of notes ref mismatches](https://github.com/rust-lang/rust/pull/46256).
* [@JRegimbal](https://github.com/JRegimbal) changed ["Types/modules" title of search tab to be more accurate](https://github.com/rust-lang/rust/pull/45898).
* [@colinmarsh19](https://github.com/colinmarsh19) removed [semicolon note](https://github.com/rust-lang/rust/pull/46258).
* [@canndrew](https://github.com/canndrew) added [docs for never primitive](https://github.com/rust-lang/rust/pull/46232).
* [@ExpHP](https://github.com/ExpHP) made [doc stubs for builtin macros reflect existing support for trailing commas](https://github.com/rust-lang/rust/pull/46260).
* [@tbu-](https://github.com/tbu-) clarified [what `-D warnings` or `-F warnings` does](https://github.com/rust-lang/rust/pull/46136).
* [@frewsxcv](https://github.com/frewsxcv) improved [documentation for slice swap/copy/clone operations](https://github.com/rust-lang/rust/pull/46219).
* [@lucasem](https://github.com/lucasem) fixed [typo in core::marker](https://github.com/rust-lang/rust/pull/46234).
* [@davidalber](https://github.com/davidalber) added [`eprint*!` to the list of macros in the `format!` family](https://github.com/rust-lang/rust/pull/46201).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings for markdown doc generation](https://github.com/rust-lang/rust/pull/46247), fixed [global doc search](https://github.com/rust-lang/rust/pull/46175), speedup [search loading when search url is received](https://github.com/rust-lang/rust/pull/46221) and removed [invalid doc link](https://github.com/rust-lang/rust/pull/46224).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781) and showed in docs [whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039).
* [@Aaronepower](https://github.com/Aaronepower) updated [Release notes for 1.22.0](https://github.com/rust-lang/rust/pull/45454).
* [@estebank](https://github.com/estebank) used [the proper term when using non-existing variant](https://github.com/rust-lang/rust/pull/46024), used [multiline text for crate conflict diagnostics](https://github.com/rust-lang/rust/pull/45946) and removed [dereference suggestion on tuple argument](https://github.com/rust-lang/rust/pull/45947).
* [@fhartwig](https://github.com/fhartwig) made [rustdoc not include self-by-value methods from Deref target](https://github.com/rust-lang/rust/pull/45645).
* [@oli-obk](https://github.com/oli-obk) added [structured suggestions for various "use" suggestions](https://github.com/rust-lang/rust/pull/46035), included [rendered diagnostic in json](https://github.com/rust-lang/rust/pull/46052) and checked [//~ERROR comments in ui tests](https://github.com/rust-lang/rust/pull/46116).
* [@sinkuu](https://github.com/sinkuu) added [doc for doing `Read` from `&str`](https://github.com/rust-lang/rust/pull/46088).
* [@ollie27](https://github.com/ollie27) fixed [broken CSS for book redirect pages](https://github.com/rust-lang/rust/pull/45998).
* [@steveklabnik](https://github.com/steveklabnik) amended [RELEASES for 1.22.1](https://github.com/rust-lang/rust/pull/46190).
* [@aqrln](https://github.com/aqrln) fixed [a typo in ToSocketAddrs documentation](https://github.com/rust-lang/rust/pull/46141).
* [@martinlindhe](https://github.com/martinlindhe) fixed [some typos](https://github.com/rust-lang/rust/pull/46157).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [path search](https://github.com/rust-lang/rust/pull/46081) and displayed [negative traits implementation](https://github.com/rust-lang/rust/pull/46134).

# Meetings

Next meeting will be on Tuesday 28th of November 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
