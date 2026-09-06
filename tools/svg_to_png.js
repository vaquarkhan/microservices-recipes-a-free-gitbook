const fs = require("fs");
const path = require("path");
const { Resvg } = require("@resvg/resvg-js");

const roots = [
  path.join(__dirname, "..", "assets", "images", "diagrams"),
  path.join(__dirname, "..", "assets", "images"),
];

function convert(svgPath) {
  const pngPath = svgPath.replace(/\.svg$/i, ".png");
  const svg = fs.readFileSync(svgPath);
  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: 1600 },
    background: "transparent",
  });
  fs.writeFileSync(pngPath, resvg.render().asPng());
  console.log(path.relative(path.join(__dirname, ".."), pngPath));
}

for (const root of roots) {
  for (const name of fs.readdirSync(root)) {
    if (!name.endsWith(".svg")) continue;
    convert(path.join(root, name));
  }
}
