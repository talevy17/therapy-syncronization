import React from "react";
import { UploadDataSection } from "./upload-data";
import { RicosViewer, upload } from "./text-viewer";

import styles from "./upload-data-tab.module.scss";

export default function UploadDataTab(props) {
  return (
    <div className={styles.container}>
      <RicosViewer contentState={upload} />
      <UploadDataSection />
    </div>
  );
}
