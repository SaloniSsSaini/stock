def ascii_chart(prices, width=8):
    min_p, max_p = min(prices), max(prices)
    if min_p == max_p:
        return "▁" * width

    step = (max_p - min_p) / width
    blocks = "▁▂▃▄▅▆▇█"

    chart = ""
    for i in range(width):
        value = prices[int(i * len(prices) / width)]
        index = int((value - min_p) / step) if step else 0
        chart += blocks[min(index, 7)]

    return chart
