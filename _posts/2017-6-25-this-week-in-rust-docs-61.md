---
layout: post
title: This Week in Rust Docs 61
date: 2017-6-25
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

After a long debate, it has been decided to keep hoedown testing/rendering by default in rustdoc. However, you can test pulldown by running rustdoc with `-Z unstable-options enable-commonmark`.

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@pwoolcoc](https://github.com/pwoolcoc) added [`allow_fail` test attribute](https://github.com/rust-lang/rust/pull/42219).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.19](https://github.com/rust-lang/rust/pull/42503).
* [@ollie27](https://github.com/ollie27) fixed [a few issues with associated consts in rustdoc](https://github.com/rust-lang/rust/pull/42865) and fixed [ICE on `use *;` in rustdoc](https://github.com/rust-lang/rust/pull/42885).
* [@frewsxcv](https://github.com/frewsxcv) fixed [a couple broken links to the reference from error messages](https://github.com/rust-lang/rust/pull/42624).
* [@rthomas](https://github.com/rthomas) updated [docs for fmt::write](https://github.com/rust-lang/rust/pull/42831), updated [docs on Error struct](https://github.com/rust-lang/rust/pull/42837), updated [docs for Debug* structs](https://github.com/rust-lang/rust/pull/42836) and updated [docs for std::fmt::format](https://github.com/rust-lang/rust/pull/42832).
* [@cengizIO](https://github.com/cengizIO) added [pager support for `rustc --explain EXXXX`](https://github.com/rust-lang/rust/pull/42732).
* [@Fourchaux](https://github.com/Fourchaux) fixed [basic typos in Doc Comments](https://github.com/rust-lang/rust/pull/42812).
* [@nagisa](https://github.com/nagisa) fix [NaN handling in is_sign_negative/positive](https://github.com/rust-lang/rust/pull/42431) and specialisation [of Iterator methods for Range](https://github.com/rust-lang/rust/pull/42534).
* [@gaurikholkar](https://github.com/gaurikholkar) adding [diagnostic code for lifetime errors with one named, one anonymous lifetime parameter](https://github.com/rust-lang/rust/pull/42669).
* [@dns2utf8](https://github.com/dns2utf8) added [hint about the return code of panic!](https://github.com/rust-lang/rust/pull/42670).
* [@Emilgardis](https://github.com/Emilgardis) fixed [wrong report on closure args mismatch when a ref is expected but not found](https://github.com/rust-lang/rust/pull/42270).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), created [more error codes](https://github.com/rust-lang/rust/pull/42519) and remove [err methods](https://github.com/rust-lang/rust/pull/42887).

# Recent doc contributions

* [@alex-ozdemir](https://github.com/alex-ozdemir) made [clearer error message for Duplicate Definition](https://github.com/rust-lang/rust/pull/42076).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) printed [the two types in the span label for transmute errors](https://github.com/rust-lang/rust/pull/42304) and made [rustc errors colorful](https://github.com/rust-lang/rust/pull/42804).
* [@ollie27](https://github.com/ollie27) used [`create_dir_all` to create output directory in rustdoc](https://github.com/rust-lang/rust/pull/42572), fixed [compiler docs yet again](https://github.com/rust-lang/rust/pull/42806), and linked [directly to associated types in rustdoc](https://github.com/rust-lang/rust/pull/42594).
* [@maccoda](https://github.com/maccoda) completed [env docs](https://github.com/rust-lang/rust/pull/42579).
* [@birkenfeld](https://github.com/birkenfeld) added [dedicated docstrings to Sum/Product impl of Result](https://github.com/rust-lang/rust/pull/42570) and simplified [FromIterator example of Result](https://github.com/rust-lang/rust/pull/42569).
* [@ucarion](https://github.com/ucarion) explicated [what "Rc" and "Arc" stand for](https://github.com/rust-lang/rust/pull/42419).
* [@cramertj](https://github.com/cramertj) changed [span label for E0435](https://github.com/rust-lang/rust/pull/42833).
* [@letheed](https://github.com/letheed) fixed [ref as mutable ref in std::rc::Rc doc](https://github.com/rust-lang/rust/pull/42825).
* [@zackmdavis](https://github.com/zackmdavis) added [extended information for E0562; impl Trait can only be a return type](https://github.com/rust-lang/rust/pull/42787).
* [@kennytm](https://github.com/kennytm) removed [most "```ignore" doc tests.](https://github.com/rust-lang/rust/pull/42777).
* [@frewsxcv](https://github.com/frewsxcv) made [additions/improvements for doc examples](https://github.com/rust-lang/rust/pull/42749).
* [@wesleywiser](https://github.com/wesleywiser) added [compile_error!](https://github.com/rust-lang/rust/pull/42620).
* [@est31](https://github.com/est31) removed [SUMMARY.md of the unstable book as its autogenerated](https://github.com/rust-lang/rust/pull/42722) and introduced [tidy lint to check for inconsistent tracking issues](https://github.com/rust-lang/rust/pull/42705).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [E0609](https://github.com/rust-lang/rust/pull/42585), added [0608](https://github.com/rust-lang/rust/pull/42568), new [error codes](https://github.com/rust-lang/rust/pull/42614) and error [codes new](https://github.com/rust-lang/rust/pull/42654).

# Meetings

Next meeting will be on Wednesday 28th of June 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
