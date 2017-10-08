---
layout: post
title: This Week in Rust Docs 76
date: 2017-10-8
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) made [rustdoc optimizations](https://github.com/rust-lang/rust/pull/44613), abd included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781), showed [in docs whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039), documented [trait impls when the type appears in the trait's generics](https://github.com/rust-lang/rust/pull/44969) and let [rustdoc print the crate version into docs](https://github.com/rust-lang/rust/pull/44989).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138).
* [@kennytm](https://github.com/kennytm) improved [doc-test: in Markdown tests, Use all of `<h1>` to `<h6>` as the test name](https://github.com/rust-lang/rust/pull/44867).
* [@federicomenaquintero](https://github.com/federicomenaquintero) improved [docs for CStr, CString, OsStr, OsString](https://github.com/rust-lang/rust/pull/44855).
* [@estebank](https://github.com/estebank) suggested [syntax when finding method on array](https://github.com/rust-lang/rust/pull/44970), warned [when assigning a block that doesn't have an implicit return](https://github.com/rust-lang/rust/pull/44881) and referred [to types using the local identifier](https://github.com/rust-lang/rust/pull/44642).
* [@sunjay](https://github.com/sunjay) documented [the process for when rustfmt/rls break](https://github.com/rust-lang/rust/pull/45098).
* [@shepmaster](https://github.com/shepmaster) don't [encourage people to ignore threading errors in the docs](https://github.com/rust-lang/rust/pull/44962).
* [@jacwah](https://github.com/jacwah) mentionned [Clone and refs in --explain E0382](https://github.com/rust-lang/rust/pull/45082).
* [@Nemo157](https://github.com/Nemo157) rendered [cfg(feature) requirements in documentation](https://github.com/rust-lang/rust/pull/44994).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [short error message-format](https://github.com/rust-lang/rust/pull/44636) and added [tabs for search for better information access](https://github.com/rust-lang/rust/pull/45055).

# Recent doc contributions

* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.21.0](https://github.com/rust-lang/rust/pull/44481).
* [@budziq](https://github.com/budziq) corrected [the CONTRIBUTING.md "External Dependencies" section](https://github.com/rust-lang/rust/pull/44664).
* [@vi](https://github.com/vi) rendered [`[src]` links for trait implementors in rustdoc](https://github.com/rust-lang/rust/pull/44920).
* [@Havvy](https://github.com/Havvy) improved [docs for size_of::<#[repr(C)]> items](https://github.com/rust-lang/rust/pull/44897).
* [@leavehouse](https://github.com/leavehouse) fixed [TcpStream::local_addr docs example code](https://github.com/rust-lang/rust/pull/44913).
* [@Pirh](https://github.com/Pirh) updated [docs for process::abort](https://github.com/rust-lang/rust/pull/44905).
* [@hunteke](https://github.com/hunteke) fixed [typo](https://github.com/rust-lang/rust/pull/45058).
* [@steveklabnik](https://github.com/steveklabnik) updated [books for next release](https://github.com/rust-lang/rust/pull/44980) and updated [mdbook](https://github.com/rust-lang/rust/pull/44977).
* [@brennie](https://github.com/brennie) updated [trait summaries for std::fmt](https://github.com/rust-lang/rust/pull/45042).
* [@vitiral](https://github.com/vitiral) added [links to headers in README and CONTRIBUTING](https://github.com/rust-lang/rust/pull/44935).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [the issue number to doc_masked's feature gate](https://github.com/rust-lang/rust/pull/45024) and let [htmldocck.py check for directories](https://github.com/rust-lang/rust/pull/44949).
* [@MaikKlein](https://github.com/MaikKlein) fixed [typo in `librustc/README.md`](https://github.com/rust-lang/rust/pull/45006).
* [@laumann](https://github.com/laumann) fixed typo: [geneartor -> generator](https://github.com/rust-lang/rust/pull/44955).
* [@dbrgn](https://github.com/dbrgn) added [trace_macros! to unstable book](https://github.com/rust-lang/rust/pull/44944).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing fnty args rustdoc](https://github.com/rust-lang/rust/pull/44892), added [missing links for AtomicBool](https://github.com/rust-lang/rust/pull/45053) and added [missing urls for Mutex](https://github.com/rust-lang/rust/pull/45017).

# Meetings

Next meeting will be on Wednesday 11th of October 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
