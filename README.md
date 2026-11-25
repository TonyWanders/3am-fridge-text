# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/TonyWanders/3am-fridge-text/rank.svg)](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/TonyWanders/3am-fridge-text/reward.svg)](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for the [The 3AM Fridge Text](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d) bounty on make.fun.

## The entry

> 3am. I have hummed all night so you could sleep, and you repay me by opening me just to stare. Go to bed.

## How it works

`main.py` writes that single line to the output target (default
`/output/entry.txt`, or the path given as the first argument, or
`$OUTPUT_PATH`). It writes only to the output target, never into the
repository, and its output is deterministic.

```sh
python3 main.py
python3 main.py /tmp/entry.txt
OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
