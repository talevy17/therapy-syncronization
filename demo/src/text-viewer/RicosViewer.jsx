import React, { PureComponent } from "react";
import { RichContentWrapper } from "wix-rich-content-wrapper";
import { RichContentViewer } from "wix-rich-content-viewer";
import { pluginDivider } from "wix-rich-content-plugin-divider/dist/module.viewer";
import { pluginImage } from "wix-rich-content-plugin-image/dist/module.viewer";
import {
  pluginTextColor,
  pluginTextHighlight,
} from "wix-rich-content-plugin-text-color/dist/module.viewer";
import { pluginLineSpacing } from "wix-rich-content-plugin-line-spacing/dist/module.viewer";

import { Paper } from "@material-ui/core";
import "./RicosViewer.scss";

export default class RicosViewer extends PureComponent {
  constructor(props) {
    super(props);
    this.plugins = [
      pluginDivider(),
      pluginImage(),
      pluginLineSpacing(),
      pluginTextColor(),
      pluginTextHighlight(),
    ];
  }
  render() {
    const { contentState, palette, isMobile, addAnchors } = this.props;
    const theme = palette
      ? { theme: "Palette", palette }
      : { theme: "Default" };
    return (
      <Paper
        className={"container"}
        variant={"elevation"}
        square
        elevation={10}
      >
        <RichContentWrapper plugins={this.plugins} {...theme}>
          <RichContentViewer
            initialState={contentState}
            isMobile={isMobile}
            addAnchors={addAnchors}
          />
        </RichContentWrapper>
      </Paper>
    );
  }
}
