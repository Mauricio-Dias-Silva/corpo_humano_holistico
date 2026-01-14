from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from anatomia.models import SistemaCorporal, Orgao, Celula
from psicologia.models import Emocao
from metabolismo.models import Substancia, ProcessoMetabolico, Desequilibrio
from simbologia.models import Chakra
from core.models import RelacaoHolistica
from core.brain import CérebroHolistico, PubMedService
import json

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # --- Chat Input ---
        user_message = self.request.GET.get('chat_msg')
        if user_message:
            brain = CérebroHolistico()
            context['chat_response'] = brain.processar_pergunta(user_message)
            context['chat_input'] = user_message
            
        # --- Scanner Logic (Legacy) ---
        query = self.request.GET.get('q')
        context['query'] = query
        
        if query:
            brain = CérebroHolistico()
            entidade = brain._buscar_entidade_generica(query)
            
            context['entidade_encontrada'] = entidade
            if entidade:
                conexoes = RelacaoHolistica.objects.filter(origem_object_id=entidade.id) | \
                           RelacaoHolistica.objects.filter(destino_object_id=entidade.id)
                context['conexoes_scanner'] = conexoes
        
        # --- General Data for Dashboard ---
        context['sistemas'] = SistemaCorporal.objects.exclude(nome__icontains="Imun").all()  # Filter out some for better UI fitting if needed
        context['emocoes'] = Emocao.objects.all()
        # context['chakras'] = Chakra.objects.all()
        
        return context

class GalaxyView(TemplateView):
    template_name = 'galaxy.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Nodes & Edges
        nodes = []
        edges = []
        
        # Helper for color/size
        def add_node(obj, group, color, size=10):
            # Lógica Dourada (Segredos)
            is_secret = False
            if obj.nome in ['Biofótons', 'Microtúbulos', 'Glândula Pineal', 'Consciência Não-Local', 'Água EZ (Zona de Exclusão)']:
                color = '#FFD700' # GOLD
                size = 30 # Huge
                is_secret = True
            
            desc = getattr(obj, 'descricao_detalhada', '') or \
                   getattr(obj, 'funcao_biologica', '') or \
                   getattr(obj, 'descricao_tecnica', '') or \
                   getattr(obj, 'funcao_micro', '') or \
                   "Sem descrição definida."
                   
            nodes.append({
                'id': str(obj.id),
                'label': obj.nome,
                'group': group,
                'color': color,
                'value': size,
                'description': desc,
                'type': "SEGREDO QUÂNTICO" if is_secret else obj.__class__.__name__
            })
            
        # 1. Add Organs (Red)
        for o in Orgao.objects.all()[:150]: 
            add_node(o, 'orgao', '#FF7F7F', 15)
            
        # 2. Add Emotions (Purple)
        for e in Emocao.objects.all():
            add_node(e, 'emocao', '#C17FFF', 20)
            
        # 3. Add Substances (Green)
        for s in Substancia.objects.all()[:50]:
            add_node(s, 'substancia', '#7FFF7F', 10)
        
        # 4. Add Cells (Blue - New)
        for c in Celula.objects.all():
            add_node(c, 'celula', '#4db8ff', 8)
            
        # 4. Add Edges (Connections)
        rels = RelacaoHolistica.objects.all()[:500]
        for r in rels:
            edges.append({
                'from': str(r.origem_object_id),
                'to': str(r.destino_object_id),
                'label': r.tipo,
                'color': {'color': 'rgba(255, 255, 255, 0.2)'}
            })
            
        context['nodes_json'] = json.dumps(nodes)
        context['edges_json'] = json.dumps(edges)
        return context

homepage = HomeView.as_view()
def galaxy_page(request):
    return GalaxyView.as_view()(request)

def body_map(request):
    return render(request, 'body_map.html')

def hologram_view(request):
    return render(request, 'hologram_map.html')

def pubmed_search(request):
    """AJAX endpoint para buscar estudos no PubMed."""
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'Query required'}, status=400)
    
    service = PubMedService()
    results = service.search(query, max_results=5)
    return JsonResponse({'studies': results})

def organ_gallery(request):
    """Galeria de órgãos 3D com modelos reais."""
    return render(request, 'organ_gallery.html')