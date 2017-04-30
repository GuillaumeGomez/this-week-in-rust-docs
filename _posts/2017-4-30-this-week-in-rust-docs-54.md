---
layout: post
title: This Week in Rust Docs 54
date: 2017-4-30
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

The jquery dependency [is being removed](https://github.com/rust-lang/rust/pull/41307) from the rustdoc javascript. When navigating in the docs, please check if everything's working as expected!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857), emitted [diagnostic when using `const` storing `Fn` as pattern](https://github.com/rust-lang/rust/pull/41434), cleaned [up callable type mismatch errors](https://github.com/rust-lang/rust/pull/41488), made [unsatisfied trait bounds note multiline](https://github.com/rust-lang/rust/pull/41489) and used [diagnostics for trace_macro instead of println](https://github.com/rust-lang/rust/pull/41520).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@topecongiro](https://github.com/topecongiro) updated [docs of 'fence'](https://github.com/rust-lang/rust/pull/41217).
* [@abonander](https://github.com/abonander) documented [the `proc_macro` feature in the Unstable Book](https://github.com/rust-lang/rust/pull/41476).
* [@ranma42](https://github.com/ranma42) generate [XZ-compressed tarballs](https://github.com/rust-lang/rust/pull/41600).
* [@alexeyzab](https://github.com/alexeyzab) fixed [error message for mismatched types](https://github.com/rust-lang/rust/pull/41547).
* [@mandeep](https://github.com/mandeep) added [generic example of std::ops::Add in doc comments](https://github.com/rust-lang/rust/pull/41612).
* [@brson](https://github.com/brson) updated [release notes for 1.17](https://github.com/rust-lang/rust/pull/41548).
* [@steveklabnik](https://github.com/steveklabnik) improved [docs on Arc<T> and Send/Sync](https://github.com/rust-lang/rust/pull/41536) and added [more ways to create a PathBuf to docs](https://github.com/rust-lang/rust/pull/41531).
* [@z1mvader](https://github.com/z1mvader) rewrote [the thread struct docs](https://github.com/rust-lang/rust/pull/41543).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [jquery dependency](https://github.com/rust-lang/rust/pull/41307), reduced [HTML output in rustdoc](https://github.com/rust-lang/rust/pull/41384) and added [better error message when == operator is badly used](https://github.com/rust-lang/rust/pull/41559).

# Recent doc contributions

* [@estebank](https://github.com/estebank) removes [display of `::{{constructor}}` on tuple struct diagnostics](https://github.com/rust-lang/rust/pull/41433) and pointed [at variable moved by closure](https://github.com/rust-lang/rust/pull/41523).
* [@tbu-](https://github.com/tbu-) specified [behavior of `write_all` for `ErrorKind::Interrupted` errors](https://github.com/rust-lang/rust/pull/41442) and fixed [a copy-paste error in `Instant::sub_duration`](https://github.com/rust-lang/rust/pull/41518).
* [@projektir](https://github.com/projektir) added [links and examples for various mspc pages](https://github.com/rust-lang/rust/pull/41438).
* [@hsivonen](https://github.com/hsivonen) explained [why zero-length slices require a non-null pointer](https://github.com/rust-lang/rust/pull/41602).
* [@frewsxcv](https://github.com/frewsxcv) bumped [mdbook dep to pick up new 'create missing' toggle feature.](https://github.com/rust-lang/rust/pull/41572).
* [@moosingin3space](https://github.com/moosingin3space) explained [process::exit in mem::forget docs](https://github.com/rust-lang/rust/pull/41636).
* [@cuviper](https://github.com/cuviper) fixed [links in RELEASES.md for 1.10.0 through 1.12.0](https://github.com/rust-lang/rust/pull/41613).
* [@steveklabnik](https://github.com/steveklabnik) cleaned [up TcpStream example](https://github.com/rust-lang/rust/pull/41526), addressed [platform-specific behavior in TcpStream::shutdown](https://github.com/rust-lang/rust/pull/41499), fixed [up vec guarantee around capacity](https://github.com/rust-lang/rust/pull/41535), clarified ["side effect" in peek's docs](https://github.com/rust-lang/rust/pull/41528), clarified [the doc index](https://github.com/rust-lang/rust/pull/41527) and used [the word 'length' in Vec::len's docs](https://github.com/rust-lang/rust/pull/41500).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [more explanation on RefCell::get_mut](https://github.com/rust-lang/rust/pull/40634) and improved [error message for invalid module location](https://github.com/rust-lang/rust/pull/41501).

# Meetings

Next meeting will be on Wednesday 3rd of May 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
