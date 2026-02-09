(deftemplate class
   (slot name)
   (multislot attributes)
   (multislot operations))
(deftemplate attribute
   (slot id)
   (slot class-name)
   (slot name)
   (slot visibility)
   (slot type))
(deftemplate operation
   (slot id)
   (slot class-name)
   (slot name)
   (slot visibility)
   (slot type))
(deftemplate dependency
   (slot client)
   (slot supplier))
(deftemplate generalization
   (slot parent)
   (slot child))
(deftemplate directedAssociation
   (slot source)
   (slot target)
   (slot multiplicity1)
  (slot multiplicity2))
(deftemplate association
   (slot source)
   (slot target)
   (slot multiplicity1)
  (slot multiplicity2))
(deftemplate composition
   (slot whole)
   (slot part)
   (slot multiplicity))
(deftemplate aggregation
   (slot whole)
   (slot part)
   (slot multiplicity))
(deffacts initial-facts
  (attribute (id attr1) (class-name Persona) (name nombre) (visibility public) (type "string"))
  (class (name Persona) (attributes attr1) (operations ))
  (attribute (id attr2) (class-name Alumno) (name id) (visibility public) (type "int"))
  (attribute (id attr3) (class-name Alumno) (name notaList1) (visibility private) (type "HashSet<nota>"))
  (class (name Alumno) (attributes attr2 attr3) (operations ))
  (attribute (id attr4) (class-name nota) (name nota) (visibility public) (type "float"))
  (class (name nota) (attributes attr4) (operations ))
  (generalization (parent Alumno) (child Persona))
  (directedAssociation (source Alumno) (target nota) (multiplicity1 1) (multiplicity2 *))
)

(defrule generate-java-code
   
   ?class <- (class (name ?class-name) (attributes $?attributes) (operations $?operations))
   (generalization (parent ?class-name) (child ?x))
   =>
   (printout t "// Java code for class " ?class-name crlf)
   (printout t "public class " ?class-name " extends " ?x " {" crlf)
   
   ;; Imprimir atributos
   (do-for-all-facts ((?attr attribute))
      (and
         (member$ (fact-slot-value ?attr id) $?attributes)
         (eq (fact-slot-value ?attr class-name) ?class-name))
      (bind ?visibility (fact-slot-value ?attr visibility))
      (bind ?type (fact-slot-value ?attr type))
      (bind ?name (fact-slot-value ?attr name))
      (printout t  "   " ?visibility " " ?type " " ?name ";" crlf))
   
   ;; Imprimir métodos
   (do-for-all-facts ((?op operation))
      (and
         (member$ (fact-slot-value ?op id) $?operations)
         (eq (fact-slot-value ?op class-name) ?class-name))
      (bind ?visibility (fact-slot-value ?op visibility))
      (bind ?type (fact-slot-value ?op type))
      (bind ?name (fact-slot-value ?op name))
      (printout t "   " ?visibility " " ?type " " ?name "()" " {" crlf
                "      // method body" crlf "   }" crlf))
   
   (printout t "}" crlf crlf)
)
                   
(defrule generate-java-code-no-inheritance
   ?class <- (class (name ?class-name) (attributes $?attributes) (operations $?operations))
   (not (generalization (parent ?class-name)))
    =>
   (printout t "// Java code for class " ?class-name crlf)
   (printout t "public class " ?class-name " {" crlf)
   
   ;; Imprimir atributos
   (do-for-all-facts ((?attr attribute))
      (and
         (member$ (fact-slot-value ?attr id) $?attributes)
         (eq (fact-slot-value ?attr class-name) ?class-name))
      (bind ?visibility (fact-slot-value ?attr visibility))
      (bind ?type (fact-slot-value ?attr type))
      (bind ?name (fact-slot-value ?attr name))
      (printout t  "   " ?visibility " " ?type " " ?name ";" crlf))
   
   ;; Imprimir métodos
   (do-for-all-facts ((?op operation))
      (and
         (member$ (fact-slot-value ?op id) $?operations)
         (eq (fact-slot-value ?op class-name) ?class-name))
      (bind ?visibility (fact-slot-value ?op visibility))
      (bind ?type (fact-slot-value ?op type))
      (bind ?name (fact-slot-value ?op name))
      (printout t "   " ?visibility " " ?type " " ?name "()" " {" crlf
                "      // method body" crlf "   }" crlf))
   
   (printout t "}" crlf crlf)
)
