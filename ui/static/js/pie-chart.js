/*--------------  coin distrubution chart END ------------*/
if ($('#coin_distribution').length) {

    zingchart.THEME = "classic";

    var myConfig = {
        "globals": {
            "font-family": "Roboto"
        },
        "graphset": [{
                "type": "pie",
                "background-color": "#fff",
                "legend": {
                    "background-color": "none",
                    "border-width": 0,
                    "shadow": false,
                    "layout": "float",
                    "margin": "auto auto 16% auto",
                    "marker": {
                        "border-radius": 3,
                        "border-width": 0
                    },
                    "item": {
                        "color": "%backgroundcolor"
                    }
                },
                "plotarea": {
                    "background-color": "#FFFFFF",
                    "border-color": "#DFE1E3",
                    "margin": "25% 8%"
                },
                "labels": [{
                    "x": "45%",
                    "y": "47%",
                    "width": "10%",
                    "text": "340 Coin",
                    "font-size": 17,
                    "font-weight": 700
                }],
                "plot": {
                    "size": 70,
                    "slice": 90,
                    "margin-right": 0,
                    "border-width": 0,
                    "shadow": 0,
                    "value-box": {
                        "visible": true
                    },
                    "tooltip": {
                        "text": "%v USD",
                        "shadow": false,
                        "border-radius": 2
                    }
                },
                "series": [{
                        "values": [1355460],
                        "text": "Cash",
                        "background-color": "#4cff63"
                    },
                    {
                        "values": [1585218],
                        "text": "Stocks",
                        "background-color": "#fd9c21"
                    },
                    {
                        "values": [1064598],
                        "text": "Crypto Currency",
                        "background-color": "#2c13f8"
                    }
                ]
            }

        ]
    };

    zingchart.render({
        id: 'coin_distribution',
        data: myConfig,
    });
}
/*--------------  coin distrubution chart END ------------*/
