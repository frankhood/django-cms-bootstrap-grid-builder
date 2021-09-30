// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  filenameHashing: false,
  runtimeCompiler: true,
  chainWebpack: config => {
    config.optimization.delete('splitChunks')
  },
  configureWebpack: {
      output: {
          library: "VueGridLayout",
          libraryExport: 'default'
      },
      performance: {
        maxEntrypointSize: 512000,
        maxAssetSize: 512000
      },
      optimization: {},
      // https://medium.com/js-dojo/how-to-reduce-your-vue-js-bundle-size-with-webpack-3145bf5019b7
      // plugins: [new BundleAnalyzerPlugin()],
  },
  css: {
      extract: false
  },
}
