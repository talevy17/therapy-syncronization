import React from "react";
import PropTypes from "prop-types";
import { RicosViewer } from "ricos-viewer";
import "ricos-viewer/dist/styles.min.css";
import { pluginDivider } from "wix-rich-content-plugin-divider/dist/module.viewer";
import { pluginImage } from "wix-rich-content-plugin-image/dist/module.viewer";
import { pluginFileUpload } from "wix-rich-content-plugin-file-upload/dist/module.viewer";
import {
  pluginTextColor,
  pluginTextHighlight,
} from "wix-rich-content-plugin-text-color/dist/module.viewer";
import { pluginLineSpacing } from "wix-rich-content-plugin-line-spacing/dist/module.viewer";
import { pluginLink } from "wix-rich-content-plugin-link/dist/module.viewer";

import { Paper } from "@material-ui/core";
import styles from "./RicosViewer.module.scss";
import "wix-rich-content-plugin-divider/dist/styles.min.css";
import "wix-rich-content-plugin-image/dist/styles.min.css";
import "wix-rich-content-plugin-link/dist/styles.min.css";
import "wix-rich-content-plugin-line-spacing/dist/styles.min.css";
import "wix-rich-content-plugin-text-color/dist/styles.min.css";
import "wix-rich-content-plugin-file-upload/dist/styles.min.css";

const plugins = [
  pluginLink(),
  pluginDivider(),
  pluginImage(),
  pluginLineSpacing(),
  pluginTextColor(),
  pluginTextHighlight(),
  pluginFileUpload(),
];

const Viewer = ({ contentState, palette, isMobile, addAnchors }) => {
  const theme = palette ? { theme: "Palette", palette } : { theme: "Default" };
  return (
    <Paper
      className={styles.viewer}
      variant={"elevation"}
      square
      elevation={10}
    >
      <RicosViewer
        content={contentState}
        plugins={plugins}
        {...theme}
        isMobile={isMobile}
        addAnchors={addAnchors}
      />
    </Paper>
  );
};

export default Viewer;

Viewer.propTypes = {
  contentState: PropTypes.object,
  pallete: PropTypes.object,
  isMobile: PropTypes.bool,
  addAnchors: PropTypes.bool,
};
