javaCodes = {
    "Replace Image":
        '''
        public static File replaceImageFile(File oldFile, File newFile) {
            if (oldFile.exists()) {
                try (FileInputStream fis = new FileInputStream(newFile);
                     FileOutputStream fos = new FileOutputStream(oldFile)) {

                    byte[] buffer = new byte[1024];
                    int length;
                    while ((length = fis.read(buffer)) > 0) {
                        fos.write(buffer, 0, length);
                    }

                } catch (IOException e) {
                }
            } else {
            }

            return oldFile;
        }         
        ''',
        "Drag and Drop Image File":
        '''
    public static void setupFileDragAndDrop(customComponents.PanelRound uploadPanel, Color dropColor, customComponents.ImageAvatar ImgAvatar) {
        final Color defaultColor = uploadPanel.getBackground();
        uploadPanel.setBackground(defaultColor);
        
        uploadPanel.setTransferHandler(new TransferHandler() {
            @Override
            public boolean canImport(TransferHandler.TransferSupport support) {
                if (!support.isDataFlavorSupported(DataFlavor.javaFileListFlavor)) {
                    return false;
                }

                try {
                    Transferable transferable = support.getTransferable();
                    @SuppressWarnings("unchecked")
                    java.util.List<File> files = (java.util.List<File>) transferable.getTransferData(DataFlavor.javaFileListFlavor);
                    if (files.size() > 0) {
                        File droppedFile = files.get(0);
                        if (!isJPEGFile(droppedFile)) {
                            showFileFormatError();
                            return false;
                        }
                        return true;
                    }
                } catch (Exception e) {
                    JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                }
                return false;
            }

            @Override
            public boolean importData(TransferHandler.TransferSupport support) {
                if (!canImport(support)) {
                    return false;
                }

                Transferable transferable = support.getTransferable();
                try {
                    @SuppressWarnings("unchecked")
                    java.util.List<File> files = (java.util.List<File>) transferable.getTransferData(DataFlavor.javaFileListFlavor);
                    if (files.size() > 0) {
                        File droppedFile = files.get(0);
                        handleDroppedFile(droppedFile,ImgAvatar);
                        return true;
                    }
                } catch (Exception e) {
                    JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                }
                return false;
            }

            private boolean isJPEGFile(File file) {
                String fileName = file.getName();
                return fileName.toLowerCase().endsWith(".jpg") || fileName.toLowerCase().endsWith(".jpeg");
            }

            private void showFileFormatError() {
                JOptionPane.showMessageDialog(null, "Only .jpg and .jpeg files are accepted.", "Invalid File Type", JOptionPane.ERROR_MESSAGE);
            }
        });
        uploadPanel.setDropTarget(new DropTarget(uploadPanel, DnDConstants.ACTION_COPY, new DropTargetAdapter() {
            public void dragEnter(DropTargetDragEvent event) {
                uploadPanel.setBackground(dropColor);
                uploadPanel.repaint();
            }

            public void dragExit(DropTargetEvent event) {
                uploadPanel.setBackground(defaultColor);
                uploadPanel.repaint();    
            }

            public void drop(DropTargetDropEvent event) {
                uploadPanel.setBackground(defaultColor);
                uploadPanel.repaint();                
                event.acceptDrop(DnDConstants.ACTION_COPY);
                Transferable transferable = event.getTransferable();
                if (transferable.isDataFlavorSupported(DataFlavor.javaFileListFlavor)) {
                    try {
                        java.util.List<File> files = (java.util.List<File>) transferable.getTransferData(DataFlavor.javaFileListFlavor);
                        if (files.size() > 0) {
                            File droppedFile = files.get(0);
                            if (isJPEGFile(droppedFile)) {
                                handleDroppedFile(droppedFile,ImgAvatar);
                                getdroppedFile = droppedFile;
                            } else {
                                showFileFormatError();
                            }
                        }
                    } catch (UnsupportedFlavorException | IOException e) {
                        JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                    }
                }
                event.dropComplete(true);
            }
            private boolean isJPEGFile(File file) {
                String fileName = file.getName();
                return fileName.toLowerCase().endsWith(".jpg") || fileName.toLowerCase().endsWith(".jpeg");
            }
            private void showFileFormatError() {
                JOptionPane.showMessageDialog(null, "Only .jpg and .jpeg files are accepted.", "Invalid File Type", JOptionPane.ERROR_MESSAGE);
            }
        }));
    }  
    
    public static void handleDroppedFile(File file,customComponents.ImageAvatar ImgAvatar) {
        ImageIcon icon = new ImageIcon(file.getAbsolutePath());
        if (icon != null && icon.getIconWidth() > 0) {
            ImgAvatar.setIcon(icon);
            ImgAvatar.repaint();
        } else {
            JOptionPane.showMessageDialog(null, file.getAbsolutePath(), "Invalid file", JOptionPane.ERROR_MESSAGE);
        }
    }      
        ''',
        "Open Image Desktop Default Image Viewer":
        '''
    public static void openImage(Icon getImage){
        String imagePath = getImage.toString();
        
        try {
            File imageFile = new File(imagePath);
            if (imageFile.exists() && (imageFile.isFile() || imageFile.canRead())) {
                Desktop.getDesktop().open(imageFile);
            } else {
                System.err.println("File does not exist or cannot be read.");
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }   
    }
        ''',
        "Get Image Using Java JFileChooser":
        '''
    public static File getImage(Component p_c) {
        JFileChooser fileChooser = new JFileChooser();
        String picturesDir = System.getProperty("user.home");
        fileChooser.setCurrentDirectory(new File(picturesDir)); 
        fileChooser.setFileFilter(new FileNameExtensionFilter("Image Files", "jpg", "jpeg"));
        int result = fileChooser.showOpenDialog(p_c);
        if (result == JFileChooser.APPROVE_OPTION) {
            return fileChooser.getSelectedFile();
        }
        return null;
    }        
        ''',
        "Image Capture using Java OpenCV Lib":
        '''
    public void startCamera() {
        capture = new VideoCapture(0);
        image = new Mat();
        byte[] imageData;
        ImageIcon icon;
        while(true){
            capture.read(image);

            final MatOfByte buf = new MatOfByte();
            Imgcodecs.imencode(".jpg", image, buf);

            imageData = buf.toArray();
            icon = new ImageIcon(imageData);
            screenCam.setIcon(icon);
            if(clicked){
                String name = JOptionPane.showInputDialog(this, "Enter image name");
                if(name == null){
                    name = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss").format(new Date());
                }
                Imgcodecs.imwrite("src/images/"+name+".jpg", image);
                clicked = false;
            }
        }
    }        
    //Start Cam
        new Thread(new Runnable(){
            @Override
            public void run() {
                startCamera();
            }
        }).start();
    
    // To stop Cam
        capture.release();
        image.release();
        '''
}

cmdCommands = {"Hide file":"attrib +h +s +r filename",
               "Unhide file":"attrib -h -s -r filename"}

jdbcCodes = {"Establish Connection":
    '''
public class Database {
    private final String url = "jdbc:mysql://localhost:3306/schooldatabase?zeroDateTimeBehavior=CONVERT_TO_NULL";
    private final String username = "root";
    private final String password = "";
    
    protected static Connection connection;
    protected static Statement statement;
    protected static PreparedStatement prepare;   
    protected static ResultSet result;
    protected static ResultSetMetaData metaData;
    
    public Database(){
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Database.connection = DriverManager.getConnection(url, username, password);
            Database.statement = connection.createStatement();
        }catch(ClassNotFoundException | SQLException e){
            e.printStackTrace();
        }              
    }  
}    
    '''}