chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 1000,
    height: 500,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		// added to make intraday visible
		timeVisible: true,
		secondsVisible: false,
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: '#00ff00',
  downColor: '#ff0000',
  borderDownColor: '#ff0000',
  borderUpColor: '#00ff00',
  wickDownColor: 'rgba(255, 144, 0, 1)',
  wickUpColor: 'rgba(255, 144, 0, 1)',
});

// Get price history and set to chart
fetch('http://localhost:5000/history')
	.then((r) => r.json())
	.then((response) => {
		console.log(response)

		candleSeries.setData(response);
	})

// Stream live data and update chart in real time
var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_15m");

binanceSocket.onmessage = function(event){
	var message = JSON.parse(event.data)
	// console.log(message.k)
	candlestick = message.k

	candleSeries.update({
		// time: Date.now(),
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}


