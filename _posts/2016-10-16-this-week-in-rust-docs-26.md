---
layout: post
title: This Week in Rust Docs 26
date: 2016-10-16
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

* [@frewsxcv](https://github.com/frewsxcv) improved [doc example for `std::borrow::Cow`](https://github.com/rust-lang/rust/pull/37187).
* [@nabeelomer](https://github.com/nabeelomer) updated [the docs for Error::description](https://github.com/rust-lang/rust/pull/37189).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [line breaks to where clauses a la rustfmt](https://github.com/rust-lang/rust/pull/37190).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [more tags display in rustdoc](https://github.com/rust-lang/rust/pull/37134), added [missing urls for io types](https://github.com/rust-lang/rust/pull/37165), added [invalid doc comment help message](https://github.com/rust-lang/rust/pull/36964), added [missing urls on Vec docs](https://github.com/rust-lang/rust/pull/37043), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).

# Recent doc contributions

* [@ollie27](https://github.com/ollie27) improved [playground run buttons in rustdoc](https://github.com/rust-lang/rust/pull/37098).
* [@est31](https://github.com/est31) colored [the question mark operator in the rustdoc output](https://github.com/rust-lang/rust/pull/37102).
* [@jfirebaugh](https://github.com/jfirebaugh) updated [E0303 to new error format](https://github.com/rust-lang/rust/pull/37060).
* [@Razican](https://github.com/Razican) improved [playground run buttons in rustdoc](https://github.com/rust-lang/rust/pull/36977).
* [@nabeelomer](https://github.com/nabeelomer) documented [that RwLock might panic](https://github.com/rust-lang/rust/pull/37141).
* [@durka](https://github.com/durka) removed [backticks in Type Aliases header in The Book](https://github.com/rust-lang/rust/pull/37119).
* [@KillTheMule](https://github.com/KillTheMule) made [explicit the fact that lifetime are descriptive](https://github.com/rust-lang/rust/pull/36997).
* [@frewsxcv](https://github.com/frewsxcv) refactored [and cleaned up rustdoc](https://github.com/rust-lang/rust/pull/37050).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) updated rustdoc [to print non-self arguments of bare functions and struct methods on their own line](https://github.com/rust-lang/rust/pull/36679).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls in io module](https://github.com/rust-lang/rust/pull/37089), added [missing urls on String module](https://github.com/rust-lang/rust/pull/37073), added [missing urls for BufWriter and BufReader](https://github.com/rust-lang/rust/pull/37115), added [missing urls in slice doc module](https://github.com/rust-lang/rust/pull/36982) and added [missing urls for hash modules](https://github.com/rust-lang/rust/pull/36961).



* [@chamoysvoice](https://github.com/chamoysvoice) updated [E0220 error format](https://github.com/rust-lang/rust/pull/36862).
* [@ollie27](https://github.com/ollie27) fixed [missing *mut T impl in rustdoc](https://github.com/rust-lang/rust/pull/36966).
* [@acrrd](https://github.com/acrrd) made [a better underline for E0057, E0060 and E0061](https://github.com/rust-lang/rust/pull/36222).
* [@angelsl](https://github.com/angelsl) mentioned [`move` keyword for lambdas in Reference](https://github.com/rust-lang/rust/pull/36929) and clarified [last element in str.{r,}splitn documentation](https://github.com/rust-lang/rust/pull/36930).
* [@wesleywiser](https://github.com/wesleywiser) fixed [documentation for `write!` on `std::fmt` page](https://github.com/rust-lang/rust/pull/36937).
* [@frewsxcv](https://github.com/frewsxcv) made a ["minor" librustdoc cleanup and refactoring](https://github.com/rust-lang/rust/pull/36903).
* [@BlueSpaceCanary](https://github.com/BlueSpaceCanary) removed [the double introduction for `cargo run`](https://github.com/rust-lang/rust/pull/36878).
* [@gavinb](https://github.com/gavinb) improved [error message and snippet for "did you mean `x`"](https://github.com/rust-lang/rust/pull/36798).
* [@kmcallister](https://github.com/kmcallister) updated [Arc docs to match new Rc docs](https://github.com/rust-lang/rust/pull/36665).
* [@christopherdumas](https://github.com/christopherdumas) updated [`includes!` documentation](https://github.com/rust-lang/rust/pull/36404).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [run button appearing when it shouldn't](https://github.com/rust-lang/rust/pull/36637), merged [E0002 into E0004](https://github.com/rust-lang/rust/pull/36909), added [missing urls for error module](https://github.com/rust-lang/rust/pull/36928), fixed [typos](https://github.com/rust-lang/rust/pull/36908) and removed [underline when run button hovered](https://github.com/rust-lang/rust/pull/37003).

# Meetings

Next meeting will be on Wednesday 17th of October 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
