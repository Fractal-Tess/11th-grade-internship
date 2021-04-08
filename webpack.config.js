const path = require("path");

module.exports = {
  devtool: "eval-source-map",
  mode: "production",
  entry: "./src/index.ts",
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: "ts-loader",
        include: [path.resolve(__dirname, "src")],
      },
    ],
  },
  resolve: {
    extensions: [".ts", ".js"],
  },
  output: {
    filename: "indexBundle.js",
    path: path.resolve(__dirname, "static/js/"),
  },
};
