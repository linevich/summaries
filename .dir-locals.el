((nil . ((eval . (progn
		   (defun make-summary-pdf ()
		     "Compiles pdf from current summary."
		     (interactive)
		     (message "Building PDF")
		     (async-shell-command
		      (concat "cd "
			      (file-name-directory buffer-file-name)
			      " && make pdf && mupdf build/build.pdf") nil nil))

		   (defvar summary-mode-map (make-sparse-keymap))
		   (define-minor-mode summary-mode
		     "Minor mode to add keybindngs to my summaries folder"
		     :init-value nil
		     :ligter: summary
		     summary-mode-map
		     )
		   
		   (define-key summary-mode-map (kbd "C-b") 'make-summary-pdf)
		   (summary-mode t))))))
