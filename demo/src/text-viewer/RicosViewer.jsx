import React from "react";
import { RichContentWrapper } from "wix-rich-content-wrapper";
import { RichContentViewer } from "wix-rich-content-viewer";
import { pluginDivider } from "wix-rich-content-plugin-divider/dist/module.viewer";
import { pluginImage } from "wix-rich-content-plugin-image/dist/module.viewer";
import {
  pluginTextColor,
  pluginTextHighlight,
} from "wix-rich-content-plugin-text-color/dist/module.viewer";
import { pluginLineSpacing } from "wix-rich-content-plugin-line-spacing/dist/module.viewer";
import { pluginLink } from "wix-rich-content-plugin-link/dist/module.viewer";

import { Paper } from "@material-ui/core";
import "./RicosViewer.scss";
import "wix-rich-content-plugin-divider/dist/styles.min.css";
import "wix-rich-content-plugin-image/dist/styles.min.css";
import "wix-rich-content-plugin-link/dist/styles.min.css";
import "wix-rich-content-plugin-line-spacing/dist/styles.min.css";
import "wix-rich-content-plugin-text-color/dist/styles.min.css";
import "wix-rich-content-wrapper/dist/styles.min.css";

const plugins = [
  pluginLink(),
  pluginDivider(),
  pluginImage(),
  pluginLineSpacing(),
  pluginTextColor(),
  pluginTextHighlight(),
];

const RicosViewer = ({ contentState, palette, isMobile, addAnchors }) => {
  const theme = palette ? { theme: "Palette", palette } : { theme: "Default" };
  return (
    <Paper className={"viewer"} variant={"elevation"} square elevation={10}>
      <RichContentWrapper plugins={plugins} {...theme}>
        <RichContentViewer
          initialState={contentState}
          isMobile={isMobile}
          addAnchors={addAnchors}
        />
      </RichContentWrapper>
    </Paper>
  );
};

export default RicosViewer;
