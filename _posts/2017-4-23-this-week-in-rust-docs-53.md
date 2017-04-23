---
layout: post
title: This Week in Rust Docs 53
date: 2017-4-23
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

* [@estebank](https://github.com/estebank) pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857), emitted [diagnostic when using `const` storing `Fn` as pattern](https://github.com/rust-lang/rust/pull/41434) and did [not show `::{{constructor}}` on tuple struct diagnostics](https://github.com/rust-lang/rust/pull/41433).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@stepancheg](https://github.com/stepancheg) improved [BufRead::is_eof documentation](https://github.com/rust-lang/rust/pull/40747).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@topecongiro](https://github.com/topecongiro) updated [docs of 'fence'](https://github.com/rust-lang/rust/pull/41217).
* [@abonander](https://github.com/abonander) documented [the `proc_macro` feature in the Unstable Book](https://github.com/rust-lang/rust/pull/41476).
* [@tbu-](https://github.com/tbu-) specified [behavior of `write_all` for `ErrorKind::Interrupted` errors](https://github.com/rust-lang/rust/pull/41442).
* [@projektir](https://github.com/projektir) added [links and examples for various mspc pages](https://github.com/rust-lang/rust/pull/41438).
* [@insaneinside](https://github.com/insaneinside) removed [display of duplicate bounds for "...but the following trait bounds were not satisfied"](https://github.com/rust-lang/rust/pull/41346).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [more explanation on RefCell::get_mut](https://github.com/rust-lang/rust/pull/40634), removed [jquery dependency](https://github.com/rust-lang/rust/pull/41307) and reduced [HTML output in rustdoc](https://github.com/rust-lang/rust/pull/41384).

# Recent doc contributions

* [@estebank](https://github.com/estebank) reduced [visual clutter of multiline start when possible](https://github.com/rust-lang/rust/pull/41245) and added [a way to get shorter spans until `char` for pointing at defs](https://github.com/rust-lang/rust/pull/41214).
* [@maccoda](https://github.com/maccoda) improved [Convert docs](https://github.com/rust-lang/rust/pull/40987).
* [@mgattozzi](https://github.com/mgattozzi) updated [`Child` docs to not have a note section](https://github.com/rust-lang/rust/pull/40812).
* [@frewsxcv](https://github.com/frewsxcv) added [top level sections to the Unstable Book.](https://github.com/rust-lang/rust/pull/41295).
* [@cengizIO](https://github.com/cengizIO) moved [E0101 and E0102 logic into new E0282 mechanism](https://github.com/rust-lang/rust/pull/41236).
* [@jonhoo](https://github.com/jonhoo) renamed [compiler_barrier to compiler_fence](https://github.com/rust-lang/rust/pull/41262).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [a list of headings to the sidebar in rustdoc](https://github.com/rust-lang/rust/pull/41280).
* [@alexeyzab](https://github.com/alexeyzab) fixed [old docs](https://github.com/rust-lang/rust/pull/41264).
* [@mbrubeck](https://github.com/mbrubeck) expanded [docs and examples for PathBuf::file_name and friends](https://github.com/rust-lang/rust/pull/41376).
* [@lukaramu](https://github.com/lukaramu) improved [std::path docs](https://github.com/rust-lang/rust/pull/41348).
* [@steveklabnik](https://github.com/steveklabnik) fixed [link to book repo](https://github.com/rust-lang/rust/pull/41365) and updated [mdbook](https://github.com/rust-lang/rust/pull/41374).
* [@durka](https://github.com/durka) removed [disclaimer from bootstrap/README.md](https://github.com/rust-lang/rust/pull/41391).
* [@mbrickn](https://github.com/mbrickn) updated [links to use https](https://github.com/rust-lang/rust/pull/41403).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [ref suggestion](https://github.com/rust-lang/rust/pull/37658), made [hoedown big comeback](https://github.com/rust-lang/rust/pull/41290), fixed [debug infinite loop](https://github.com/rust-lang/rust/pull/41342), fixed [line display for hoedown](https://github.com/rust-lang/rust/pull/41405) and re-enabled [hoedown by default](https://github.com/rust-lang/rust/pull/41431).

# Meetings

Next meeting will be on Wednesday 26th of April 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
