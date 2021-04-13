const path = require("path");

module.exports = {
  devtool: "eval-source-map",
  mode: "production",
  entry: "./src/faceapi.ts",
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
    filename: "faceapiBundle.js",
    path: path.resolve(__dirname, "static/js/"),
  },
};
