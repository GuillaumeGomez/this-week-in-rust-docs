---
layout: post
title: This Week in Rust Docs 73
date: 2017-9-17
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) hid [internal types/traits from std docs via new #[doc(masked)] attribute](https://github.com/rust-lang/rust/pull/44026) and made [rustdoc optimizations](https://github.com/rust-lang/rust/pull/44613).
* [@gaurikholkar](https://github.com/gaurikholkar) added [E0623 for return types - both parameters are anonymous](https://github.com/rust-lang/rust/pull/44124) and extended [E0623 for earlybound and latebound for structs](https://github.com/rust-lang/rust/pull/44549).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138).
* [@laumann](https://github.com/laumann) added [suggestions for misspelled method names](https://github.com/rust-lang/rust/pull/44297).
* [@zackmdavis](https://github.com/zackmdavis) added [comparison operators to must-use lint (under `fn_must_use` feature)](https://github.com/rust-lang/rust/pull/44103).
* [@bluss](https://github.com/bluss) documented [thread builder panics for nul bytes in thread names](https://github.com/rust-lang/rust/pull/44651).
* [@oli-obk](https://github.com/oli-obk) removed [suggestion of placing `use` statements into expanded code](https://github.com/rust-lang/rust/pull/44215).
* [@Havvy](https://github.com/Havvy) expanded [size_of docs](https://github.com/rust-lang/rust/pull/44648).
* [@frewsxcv](https://github.com/frewsxcv) indicated [how ChildStd{in,out,err} FDs are closed](https://github.com/rust-lang/rust/pull/44625) and fixed [incorrect `into_inner` link in docs](https://github.com/rust-lang/rust/pull/44622).
* [@eddyb](https://github.com/eddyb) pretty-printed [unevaluated expressions in types](https://github.com/rust-lang/rust/pull/44562).
* [@nikomatsakis](https://github.com/nikomatsakis) reworked [the README.md for rustc and add other readmes](https://github.com/rust-lang/rust/pull/44505).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.21.0](https://github.com/rust-lang/rust/pull/44481).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [deref suggestion](https://github.com/rust-lang/rust/pull/43870), added [display of cfg in rustdoc](https://github.com/rust-lang/rust/pull/44165), updated [codeblock color](https://github.com/rust-lang/rust/pull/44397), removed [small id false positive in rustdoc html diff](https://github.com/rust-lang/rust/pull/44350), added [short error message-format](https://github.com/rust-lang/rust/pull/44636) and added [pub visibility for methods as well](https://github.com/rust-lang/rust/pull/44554).

# Recent doc contributions

* [@gaurikholkar](https://github.com/gaurikholkar) extended [E0623 for LateBound and EarlyBound Regions](https://github.com/rust-lang/rust/pull/44079) and extended [E0623 for fn items](https://github.com/rust-lang/rust/pull/44516).
* [@steveklabnik](https://github.com/steveklabnik) updated [mdbook](https://github.com/rust-lang/rust/pull/44430).
* [@tommyip](https://github.com/tommyip) added [doc example to String::as_mut_str](https://github.com/rust-lang/rust/pull/44453), added [doc example to String::as_str](https://github.com/rust-lang/rust/pull/44449) and added [doc example to str::from_boxed_utf8_unchecked](https://github.com/rust-lang/rust/pull/44497).
* [@smt923](https://github.com/smt923) added [short doc examples for str::from_utf8_mut](https://github.com/rust-lang/rust/pull/44472).
* [@toidiu](https://github.com/toidiu) updated [documentation to demonstrate mutability](https://github.com/rust-lang/rust/pull/44467).
* [@napen123](https://github.com/napen123) added [doc examples for str::as_bytes_mut](https://github.com/rust-lang/rust/pull/44457) and added [doc examples to str::from_utf8_unchecked_mut](https://github.com/rust-lang/rust/pull/44477).
* [@frehberg](https://github.com/frehberg) extended [UdpSocket API doc](https://github.com/rust-lang/rust/pull/44378).
* [@est31](https://github.com/est31) moved [the man directory to a subdirectory](https://github.com/rust-lang/rust/pull/44413), used ["avoid" instead of "disable" because it's a better word there](https://github.com/rust-lang/rust/pull/44569) and fixed [mispositioned error indicators](https://github.com/rust-lang/rust/pull/44386).
* [@joshlf](https://github.com/joshlf) documented [std::thread::LocalKey limitation with initializers](https://github.com/rust-lang/rust/pull/44396).
* [@jonhoo](https://github.com/jonhoo) mentionned [that HashMap::new and HashSet::new do not allocate](https://github.com/rust-lang/rust/pull/44609).
* [@ollie27](https://github.com/ollie27) removed [double count of ids when using --enable-commonmark](https://github.com/rust-lang/rust/pull/44368).
* [@rwakulszowa](https://github.com/rwakulszowa) added [an example of std::str::encode_utf16](https://github.com/rust-lang/rust/pull/44521).
* [@frewsxcv](https://github.com/frewsxcv) clarified [return type of `String::from_utf16_lossy`](https://github.com/rust-lang/rust/pull/44572).
* [@adlerd](https://github.com/adlerd) fixed [drain_filter doctest](https://github.com/rust-lang/rust/pull/44534).
* [@Havvy](https://github.com/Havvy) fixed [example in transmute](https://github.com/rust-lang/rust/pull/44536).
* [@42triangles](https://github.com/42triangles) added [an example for `std::str::into_boxed_bytes()`](https://github.com/rust-lang/rust/pull/44485).
* [@carols10cents](https://github.com/carols10cents) updated [label explanations](https://github.com/rust-lang/rust/pull/44476).
* [@tbu-](https://github.com/tbu-) clarified [the behavior of UDP sockets wrt. multiple addresses in `connect`](https://github.com/rust-lang/rust/pull/44388).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilised [compile_fail](https://github.com/rust-lang/rust/pull/43949), fixed [rendering of const keyword for functions](https://github.com/rust-lang/rust/pull/44254), reduced [false positives number in rustdoc html diff](https://github.com/rust-lang/rust/pull/44347) and updated [openoptions docs](https://github.com/rust-lang/rust/pull/44541).

# Meetings

Next meeting will be on Wednesday 20th of September 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
