const path = require('path');
	module.exports = {
		entry: './.sphinx/_static/js/cookie-policy-init.js',
		output: {
			filename: 'bundle.js',
			path: path.resolve(__dirname, '.sphinx/_static/js')
		},
		module: {
			rules: [
				{
					test: /\.js$/,
					exclude: /node_modules/,
					use: {
						loader: 'babel-loader',
						options: {
							presets: ['@babel/preset-env']
						}
					}
				}
			]
		}
	};